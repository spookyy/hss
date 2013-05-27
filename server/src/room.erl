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
    gen_server:cast(RoomId, {player_exit, PlayerId}).
%%%==================================================================
%%% gen_server callbacks
%%%==================================================================
init([LocalName]) ->
    {ok,#state{self_id=LocalName}}.

handle_call(stop, _From, State)->
    {stop, normal, stopped, State};

handle_call({player_enter, PlayerId}, _From, State) ->
    PlayerCount = length(State#state.players),
    case PlayerCount < 2 of
	true ->
	    Players = State#state.players,
	    NewPlayers = [PlayerId|Players],
	    io:format("player ~p enters room ~p~n", [PlayerId, State#state.self_id]),
	    io:format("room ~p has players: ~p~n", [State#state.self_id, NewPlayers]),
	    %% notify hall some has entered this room
	    RoomId = State#state.self_id,
	    hall:notify(RoomId,PlayerCount),
	    {reply, "ok", State#state{players=NewPlayers}};
	false ->
	    {reply, "nok", State}
    end;

handle_call(_Request, _From, State)->
    {reply, handle_call, State}.

handle_cast({player_exit, PlayerId}, State) ->
    Players = State#state.players,
    NewPlayers = lists:delete(PlayerId, Players),
    {noreply, State#state{players=NewPlayers}};

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
