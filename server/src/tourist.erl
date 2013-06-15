%% when people get into the hall, it's just a tourist containing little data. It may quit or logout any minute.
%% code to be done here
-module(tourist).
-include("identity.hrl").
-export([
	 create/2,
	 loop/2
	]).

create(Sock,TstInfo) ->
    spawn(fun() -> tourist:loop(Sock,TstInfo) end).

loop(Sock,TstInfo) ->
    inet:setopts(Sock, [{active, once}]),
    receive
	{tcp, Sock, Data} ->
	    %% do some thing
	    TouristId = TstInfo#identity.id,
	    TId = "id_" ++ integer_to_list(TouristId),
	    %% extract which room
	    Room = binary_to_list(Data),
	    io:format("TId ~p want to enter room ~p~n", [TId,Room]),
	    Join_room = room:player_enter(list_to_atom(Room), list_to_atom(TId)),
	    case Join_room of 
		"ok" ->
		    {ok, Pid} = player:start(list_to_atom(TId),Sock),
		    gen_tcp:controlling_process(Sock, Pid),
		    gen_tcp:send(Sock,"ok"),
		    loop(Sock, TstInfo);
		"nok" ->
		    gen_tcp:send(Sock, Join_room),
		    loop(Sock,TstInfo)
	    end;
	{tcp_closed, Sock} ->
	    %% do some thing
	    io:format("tourist quit"),
	    gen_tcp:close(Sock);
	{tcp_error, Sock, Reason} ->
	    io:format("tourist:tcp error ~n"),
	    exit(Reason)
    end.

