%%%------------------------------------------------------------------
%%% @author Samuel <qmchen2011@126.com>
%%% [http://qmchen2011.xicp.net]
%%% @copyright 2013 - HSS
%%% @doc HSS server. This module defines a server process that
%%% listens for incoming TCP connections and create new processes
%%% @end
%%%------------------------------------------------------------------

-module(hall).

-behaviour(gen_server).

-include("identity.hrl").

%% API
-export([
	 start/0,
	 stop/0,
	 login/1,
	 logout/1,
	 notify/2
	]).

%% gen_server callbacks
-export([init/1,handle_call/3,handle_cast/2, handle_info/2, code_change/3, terminate/2]).

-define(SERVER, ?MODULE).
-define(DEFAULT_PORT, 6666).
-record(state,{tourists=[], rooms=[]}).

%%%==================================================================
%%% API
%%%==================================================================

start() ->
    gen_server:start_link({local,?MODULE}, ?MODULE, [], []).

stop() ->
    gen_server:cast(?SERVER, stop).

login(Id) ->
    gen_server:call(?MODULE, {login, Id}).

logout(Id) ->
    gen_server:call(?MODULE, {logout, Id}).

notify(RoomId, PlayersCount) ->
    io:format("hall:notify~n"),
    gen_server:cast(?MODULE, {room_status_changed, RoomId, PlayersCount}).

%%%==================================================================
%%% gen_server callbacks
%%%==================================================================

init([]) ->
    %% start mnesia which stores all players' ID  info

    case gen_tcp:listen(?DEFAULT_PORT,[binary, {packet,0}, {active,once}, {reuseaddr, true}]) of %% here!!!  think about the arg {active,false}
	{ok, ListenSock} ->
	    io:format("gen_tcp:listen works~n"),
	    spawn_link(fun() -> server_accept(ListenSock) end);
	{error, Reason} ->
	    exit(Reason)
    end,
    
    Rooms = ets:tab2list(room),
    io:format("~p~n",[Rooms]),
    [begin
	 create_room(RoomId),
	 io:format("~p~n",[RoomId])
     end
     || {room,RoomId, _Name, _PN, _Status} <- Rooms],
    io:format("pingpong~n"),
    {ok, #state{rooms=Rooms}}.

%% server process always listen request from client, and spawn a new pproces to handle it
server_accept(LSock) ->
    case gen_tcp:accept(LSock) of
	{ok, Sock} ->
	    io:format("gen_tcp:accept works~n"),
	    %create_new_process to handle new request
	    Pid = spawn(conn_handler, loop, [Sock]),
	    gen_tcp:controlling_process(Sock, Pid),
	    server_accept(LSock);
	{error,Reason} ->
	    exit(Reason)
    end.

handle_call({login, Id}, _From, State) ->
    Tourist = #tourist{ id=Id},
    Tourists = State#state.tourists,
    NewTourists = [Tourist|Tourists],
    {reply,login, State#state{tourists = NewTourists}};

handle_call({logout, Id}, _From, State) ->
    Tourist = #tourist{ id=Id},
    Tourists = State#state.tourists,
    NewTourists = lists:delete(Tourist,Tourists),
    {reply,logout, State#state{tourists = NewTourists}};

handle_call(_Request, _From, State) ->
    Reply = ok,
    {reply, Reply, State}.

handle_cast({room_status_changed, RoomId, PlayersCount}, State) ->
    Rooms = State#state.rooms,
    [begin
	 gen_server:cast(RoomId,{room_status_changed, State})
     end
     || {room, RoomId, _, _, _} <- Rooms],
    io:format("hall:handle_cast <-> notify~n"),
    {noreply, State};

handle_cast(stop, State) ->
    {stop, normal, State}.

handle_info(_Info, State) ->
    {noreply, State}.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.

terminate(_Reason, _State) ->
    ok.

%%%==================================================================
%%% internal apis
%%%==================================================================

create_room(RoomId) ->
    io:format("create room~n"),
    room:create(RoomId).

