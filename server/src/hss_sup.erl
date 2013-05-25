%% -*- root supervisor -*-

-module(hss_sup).

-behaviour(supervisor).

%% API
-export([
	 start_link/0,
	 start_child/1
	]).

%% Supervisor callbacks

-export([init/1]).

-define(SUPERVISOR, ?MODULE).

start_link() ->
    supervisor:start_link({local, ?SUPERVISOR}, ?MODULE, []).

%% add worker process dynamically
start_child(ChildSpec) ->
    io:format("hss_sup:~p~n",[ChildSpec]),
    supervisor:start_child(?SUPERVISOR, ChildSpec).

init([]) ->
    Server = {hall, {hall, start, []},
	     permanent, 2000, worker, [hall]},
    Children = [Server],
    RestartStrategy = {one_for_one, 0, 1},
    {ok, {RestartStrategy, Children}}.


