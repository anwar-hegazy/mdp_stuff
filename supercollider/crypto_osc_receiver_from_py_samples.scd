//play samples
//start by doing this
s.boot;
s.startAliveThread;
ServerBoot.add { s.initTree };

// setup

//only one sample
~b = Buffer.read(s, "/Users/cta/Desktop/Kind.aif" );

//multiple samples
~arrayOfBuffers = "/Users/cta/Desktop/samples/*".pathMatch.collect{ | file | Buffer.read( s, file ); };

//
(
SynthDef(\play, { | amp = 0.0, trig, bufnum |
	var env, sig;

 	env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
	sig = PlayBuf.ar( 1, bufnum, BufRateScale.kr( bufnum ), loop: 1 ) * env;
	Out.ar( [ 0, 1 ], sig * amp );
}).add;
)

//run the synth on the server and play it
h = Synth( \play, [ \bufnum, ~arrayOfBuffers[0], \amp, 0.3, \trig, 0 ]);
//turn it off
h.set(\trig, 0 );

(
x = OSCFunc({ |msg, time, addr, port |
	var incoming;
	incoming = msg[1];
	("incoming is " + incoming ).postln;
	h.set(\bufnum, ~arrayOfBuffers[incoming.asInt], \amp, 0.4, \trig, 1 );
	}, '/sample');
)

//
Server.killAll;