%%%------------------------------------------------------------------
%%% @author Samuel <qmchen2011@126.com>
%%% [http://qmchen2011.xicp.net]
%%% @copyright 2013 - HSS
%%% @doc Player fsm. This module defines a player process that
%%% holds all data when playing game.
%%% @end
%%%------------------------------------------------------------------

%% when tourist get into any room, it becomes a player. 
%% It will be implemented as gen_fsm
%% code to be done here
-module(player).
-behavior(gen_fsm).

-record(player,{state}).
%% API
-export([
	 start/1,
	 start_round/1,
	 do_nothing/1
	]).
%% ALL STATE APIS
-export([
	 round_start/2,
	 do_nothing/2
	]).
%% gen_server callbacks
-export([
	 init/1, 
	 handle_event/3, 
	 handle_sync_event/4,
	 handle_info/3,
	 terminate/3,
	 code_change/4
	]).

%%%==================================================================
%%% API
%%%==================================================================

start(LocalName) ->
    
    gen_fsm:start({local, LocalName}, ?MODULE, [], []).

start_round(LocalName) ->
    gen_fsm:send_event(LocalName, round_start).

do_nothing(LocalName) ->
    gen_fsm:send_event(LocalName, do_nothing).
%%%==================================================================
%%% gen_fsm states
%%%==================================================================
do_nothing(Event, StateData) ->
    case Event of
	round_start ->
	    io:format("now game started~n"),
	    {next_state, round_start, StateData};
	_ ->
	    io:format("if not start game, then do nothing~n"),
	    {next_state, do_nothing, StateData}
    end.

round_start(Event, StateData) ->
    case Event of
	do_nothing ->
	    io:format("now do nothing"),
	    {next_state, do_nothing, StateData};
	 _ ->
	    {next_state, do_nothing, StateData}
    end.
	    


%%%==================================================================
%%% gen_fsm callbacks
%%%==================================================================
init([]) ->
    %%
    State = #player{state=do_nothing},
    {ok, do_nothing, State}.

handle_event(_Event, _StateName, State) ->
    {next_state, _StateName, State}.

handle_sync_event(_Event, _From, _StateName, State)->
    {next_state, _StateName, State}.

handle_info(_Info, _StateName, StateData) ->
    {next_state, _StateName, StateData}.

terminate(_Reason, _StateName, _State) ->
    ok.

code_change(_OldVsn, _StateName, _StateData, _Extra) ->
    {ok, _StateName, _StateData}.
