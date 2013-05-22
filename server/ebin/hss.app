%% -*- mode: Erlang; fill-column: 75; comment-column: 50; -*-

{application, hss,
  [{descrption, "HSS server for erlang solution"},
   {vsn, "0.1.0"},
   {modules,[hss_app,
	     hss_sup,
	     hall]},
   {registered,[hss_sup]},
   {applications, [kernel,stdlib]},
   {mod, {hss_app, []}}
  ]
}.
