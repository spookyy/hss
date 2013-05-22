-module(room).
-compile(export_all).

-behavior(gen_server).

-include("identity.hrl").

-record(state,{self_id=undefined, players=[]}).

-export([create/1,
	 stop/0,
         player_enter/2,
	 player_exit/2]).

-export([
	init/1,
	handle_call/3,
	handle_cast/2,
	handle_info/2,
	terminate/2,
	code_change/3
	]).

%%%==================================================================
%%% external apis
%%%==================================================================
create(LocalName) ->
    gen_server:start_link({local, LocalName}, ?MODULE, [LocalName],[]).

stop()->
    gen_server:call(?MODULE,stop).

player_enter(RoomId,PlayerId) ->
    gen_server:call(RoomId, {player_enter, PlayerId}).

player_exit(RoomId,PlayerId) ->
    gen_server:call(RoomId, {player_exit, PlayerId}).
%%%==================================================================
%%% gen_server callbacks
%%%==================================================================
init([LocalName]) ->
    {ok,#state{self_id=LocalName}}.

handle_call({player_enter, PlayerId},_From, State) ->
    Players = State#state.players,
    NewPlayers = [PlayerId|Players],
    {reply, "players enter", #state{players=NewPlayers}};
handle_call({player_exit, PlayerId},_From, State) ->
    Players = State#state.players,
    NewPlayers = lists:delete(PlayerId, Players),
    {reply, "players exit", #state{players=NewPlayers}};

handle_call(stop, _From, State)->
    {stop, normal, stopped, State};

handle_call(_Request, _From, State)->
    {reply, handle_call, State}.

%%  notify hall that status changed
handle_cast(status_changed, State) ->
    Players = State#state.players,
    PlayersCount = length(Players),
    hall:notify(State#state.self_id,PlayersCount),
    {noreply, State};
handle_cast( {room_status_changed, Info}, State) ->
    io:format("room_status_changed:~p~n",[Info]),
    {noreply, State};
handle_cast(_Request, State) ->
    {noreply, State}.
handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.
