%% -*- root supervisor -*-

-module(hss_sup).

-behaviour(supervisor).

%% API
-export([start_link/0]).

%% Supervisor callbacks

-export([init/1]).

-define(SERVER, ?MODULE).

start_link() ->
    supervisor:start_link({local, ?SERVER}, ?MODULE, []).

init([]) ->
    Server = {hall, {hall, start, []},
	     permanent, 2000, worker, [hall]},
    Children = [Server],
    RestartStrategy = {one_for_one, 0, 1},
    {ok, {RestartStrategy, Children}}.
