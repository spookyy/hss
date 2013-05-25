-module(conn_handler).
-include("identity.hrl").
-export([loop/1]).

%% every connection respond one process, Yeah, that's what I do
loop(Sock) -> 
    inet:setopts(Sock,[{active,once}]),
    % receive data from client
    receive
	{tcp, Sock, Data} ->
	    % data handling, ready for next message
	    Rcv_data = binary_to_list(Data),
	    Rcv_list = string:tokens(Rcv_data, "@"),
	    case length(Rcv_list) =/= 3 of
		true ->
		    gen_tcp:send(Sock, "Please make sure that name or password all be right");
		false ->
		    case hd(Rcv_list) of
			"login" ->
			    [Name,Password] = tl(Rcv_list),
			   
			    io:format("login is ok~n"),
			    %% check whether there is already in mnesi
			    case mnesia:dirty_index_read(identity, Name,name) of
				[] ->
				    gen_tcp:send(Sock,"Sir, you haven't registered yet");
				[#identity{id=_Id,name=Name,password=Password}] ->
				    %% here player should entered the game hall
				    %% first get the room info
				    gen_tcp:send(Sock,"ok"),
				    RoomsInfo = hall:get_room_info(),
				    [ begin
				    	  StringRI = tuple_to_string(RoomInfo),
				    	  gen_tcp:send(Sock, StringRI)
				      end|| RoomInfo <- RoomsInfo],
				    TPid = tourist:create(Sock,#identity{id=_Id,name=Name,password=Password}),
				    gen_tcp:controlling_process(Sock, TPid),
				    exit(self(),normal);
				_ ->
				    gen_tcp:send(Sock,"Sir, you password is wrong, relogin or register")
			    end;
		        "register" ->		
			    [Name,Password] = tl(Rcv_list),
			    F = fun() ->
					%% check whether there is already in mnesia
				       	case mnesia:index_read(identity, Name,name) of
					    [] ->
						Last_id = mnesia:last(identity),
			  			Id = Last_id + 1,
						mnesia:write(#identity{id=Id,name=Name,password=Password});
					    _ ->
						gen_tcp:send(Sock, "Sir, you already registered!")      				
					end
				end,
			    {atomic, ResultOfFun} = mnesia:transaction(F),
			    io:format("register :~p~n",[ResultOfFun]);
			_ ->
                            gen_tcp:send(Sock, "Some error happens, waiting to be fixed")
		    end
	    end,
	    loop(Sock);
	{tcp_closed, Sock} ->
	    io:format("tcp closed~n"),
	    gen_tcp:close(Sock);
	{tcp_error, Sock, Reason} ->
	    io:format("tcp error"),
	    exit(Reason)
    end.

tuple_to_string({room,Id, RN, PN, Status}=_Tuple) ->
    lists:concat([room," ", Id, " ", RN, " ", PN, " ", Status]). 
