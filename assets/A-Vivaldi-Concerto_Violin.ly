\version "2.18.2"

\header {
  title = "Concerto"
  instrument = "for Oboe, Violin, String and Basso Continuo"
  composer = "A. Vivaldi"
  opus = "RV 548"
  tagline = ""
}


global= {
  \key bes \major
  \time 4/4
}

violinSolo= \new Voice \relative a' {
  \set Staff.instrumentName = #"Violin Solo"
  \clef violin
  \tempo "Allegro"  
  bes16\f a bes c d8 ees f4 r16 f g a
  bes( a) g f ees d c bes a8 g f4
  bes16\p a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes f4 r
  f'16\p bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d
  d4\trill\>( c\!)\breathe c16\f f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16( f g8) g,16( a bes8)
  % Measure 10
  a8 f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f( g aes)
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g( a bes)
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a'
  \mark \default 
  bes4 r r2
  r1
  r2 r4 r8 bes,\upbow
  % Measure 20
  d16( ees) f4 d8\upbow ees16( f) g4 ees8\upbow
  f g16( a) bes8 d, e c'16( bes) a\downbow g f ees 
  d c bes a bes8 f' f4\trill f\trill
  f\trill f\trill f\trill f\trill
  f\trill f8 d c16 d e8 e16 f g8
  f f, r d' d16 bes f'4 d8
  d\trill c r c c16 a f'4 c8
  c\trill bes r bes e16 f g8 g,16 a bes8
  bes a r a'\p c16 bes a8 c16 bes a8
  c16 bes a8 c16 bes a8 c16\cresc bes a8 c16 bes a8
  % Measure 30
  a16 g f8 bes16 a g8 f4\mf r
  c r16 c d e f e d c bes a g f 
  e8 d c4 c'16\p f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8 
  d4 r d16 g, d'4 f8 
  e16 g, e'4 g8 d16 g, d'4 f8
  e4 r e16\f a, e'4 g8
  f16 a, f'4 a8 e16 a, e'4 g8
  f4 r8 f\ff g16 a bes a g f e d
  cis a e'4 g8 f d e cis
  % Measure 40
  \mark \default 
  d4 r r2
  d8 a'( bes) d,( cis) bes' a16( g) f( e)
  \tuplet 6/4{a,16\p( d f) f( d a)}\tuplet 6/4{a( d f) f( d a)}\tuplet 6/4{a( d f) f( d a)}\tuplet 6/4{a( d f) f( d a)}
  \tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}
  \tuplet 6/4{a( d f) f( d a)}\tuplet 6/4{a( d f) f( d a)}\tuplet 6/4{d,( bes' g') g( bes, d,)}\tuplet 6/4{d( bes' g') g( bes, d,)}
  \tuplet 6/4{a'( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}
  \tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{a( cis e) e( cis a)}\tuplet 6/4{d,( c' fis) fis( c d,)}\tuplet 6/4{d( c' fis) fis( c d,)}
  \tuplet 6/4{d( c' fis) fis( c d,)}\tuplet 6/4{d( c' fis) fis( c d,)}\tuplet 6/4{d( c' fis) fis( c d,)}\tuplet 6/4{d( c' fis) fis( c d,)}
  \tuplet 6/4{d( bes' g') g( bes, d,)}\tuplet 6/4{d( bes' g') g( bes, d,)}\tuplet 6/4{ees( c' g') g( c, ees,)}\tuplet 6/4{ees( c' g') g( c, ees,)}
  \tuplet 6/4{ees( c' g') g( c, ees,)}\tuplet 6/4{ees( c' g') g( c, ees,)}\tuplet 6/4{d( a' fis') fis( a, d,)}\tuplet 6/4{d( a' fis') fis( a, d,)}
  % Measure 50
  \tuplet 6/4{d( a' fis') fis( a, d,)}\tuplet 6/4{d( a' fis') fis( a, d,)}\tuplet 6/4{d( bes' g') g( bes, d,)}\tuplet 6/4{d( bes' g') g( bes, d,)}
  \tuplet 6/4{d( a' g') g( a, d,)}\tuplet 6/4{d( a' g') g( a, d,)}\tuplet 6/4{d( a' fis') fis( a, d,)}\tuplet 6/4{d( a' fis') fis( a, d,)}
  g'\f fis g a bes8 c d4 r8 fis,\p
  a16 fis e d a' fis e d bes'8 g r g
  fis16 d a'4 fis8 g16 d bes'4 g8 
  fis16\f d a'4 fis8 g bes, a fis'
  bes,16 a bes8 c16 bes c8 d16 c bes8 r g
  bes16 a g8 a16 g fis8 g g, r bes''
  \mark \default
  d16( bes) bes( g) g( f) f( ees) ees4. c'8
  c16( a) a( f) f( ees) ees( d) d4. bes'8
  % Measure 60
  bes16( g) g( ees) ees( d) d( c) c( a) a( f) f( ees) ees( d) 
  d4 r8 d' \appoggiatura ees32 d16 c d8 \appoggiatura ees32 d16 c d8
  c4 r8 a' \appoggiatura d,32 c16 bes c8 \appoggiatura d32 c16 bes c8
  bes4 r8 f' \appoggiatura c32 bes16 a bes8 \appoggiatura c32 bes16 a bes8
  c16 f, c'4 f8 d16 f d4 f8
  c16 f, c'4 f8 d4 r
  r r8 d ees g4 c,8
  d f4 bes,8 c ees4 a,8
  bes4 r8 bes f' f f f
  g f16 ees d c d ees f8 ees16 d c bes c d
  % Measure 70
  ees8 d16 c bes a bes c d4 r8 d 
  c16 bes c8 bes16 a bes8 a16 g a8 a d
  c16 bes c8 bes16 a bes8 a16 g a8 r c'
  d2 d8 c16 bes a g a bes 
  c2 c8 bes16 a g f g a 
  bes2 bes8 a16 g f es f g 
  a2 bes4 r16 d, ees f 
  bes,4 r16 d ees f bes,4 r16 d ees f
  bes,4 r16 d ees f bes, d c bes a8. bes16
  bes  a bes c d8 ees f4 r16 f g a
  % Measure 80
  bes a g f ees d c bes a8 g f4
  bes16 a bes c d8 ees f4 r16 f g a
  bes a g f ees d c bes f4 r
  \mark \default
  f'16 bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d 
  d4(\trill c)\breathe c16 f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16f g8 g,16 a bes8
  a f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f g aes
  % Measure 90
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g a bes
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a' bes4\fermata r r2
  \bar "|."
}

OboeSolo= \new Voice \relative a' {
  \set Staff.instrumentName = #"Oboe Solo"
  \clef violin
  \tempo "Allegro"  
    bes16\f a bes c d8 ees f4 r16 f g a
  bes( a) g f ees d c bes a8 g f4
  bes16\p a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes f4 r
  f'16\p bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d
  d4\trill\>( c\!)\breathe c16\f f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16( f g8) g,16( a bes8)
  % Measure 10
  a8 f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f( g aes)
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g( a bes)
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a'
  \mark \default 
  bes4 r8 bes, d16( ees) f4 d8
  ees16( f) g4 ees8 f g16( a) bes8 d,8
  ees c'16( bes) a g f ees d c bes a bes4
  r1
  r
  r4 r8 d d16 bes f'4 d8
  d\trill c r c c16 a f'4 c8 
  c\trill bes r bes ees16 f g8 g,16 a bes8
  bes a r f' f4\trill f\trill
  f\trill f\trill f\trill f\trill 
  f\trill f8 d c16 d e8 e16 f g8 
  f f, r f'\p a16 g f8 a16 g f8
  a16 g f8 a16 g f8 a16\cresc g f8 a16 g f8
  f16 ees d8 g16 f ees8 f4\mf r
  c r16 c d e f e d c bes a g f 
  e8 d c4 c'16\p f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8 
  d4 r d16 g, d'4 f8 
  e16 g, e'4 g8 d16 g, d'4 f8
  e4 r e16\f a, e'4 g8 
  f16 a, f'4 a8 e16 a, e'4 g8
  f4 r8 f\ff g16 a bes a g f e d 
  cis a e'4 g8 f d e cis
  \mark \default 
  d a'( bes) d,( cis) bes' a16( g) f( e) 
  f8 d r4 r2
  f2\f~ f8 f16 g a8 f 
  e2~ e8 f16 e g8 e 
  d2~ d8 e16 d bes'8 d,
  cis4 r16 a cis e g2~
  g8 fis16 g a g fis e fis8 a4 d,8~
  d c4 a'8 c, bes16 c d c bes a 
  bes4 r8 g' ees2~
  ees8 g ees c fis2~
  fis8 a fis d bes'16 a g8 bes16 a g8 
  a4. d,8 a'16 g fis8 a16 g fis8
  g16\f fis g a bes 8 c d4 r8 fis,\p
  a16 fis e d a' fis e d bes'8 g r g 
  fis16 d a'4 fis8 g16 d bes'4 g8 
  fis16\f d a'4 fis8 g bes, a fis'
  g16 fis g8 a16 g a8 bes16 a g8 r bes, 
  d16 c bes8 c16 bes a8 bes16 a g8 r4
  \mark \default
  r r8 d' g16( ees) ees( c) c( bes) bes( a)
  a4. f'8 f16( d) d( bes) bes( aes) aes( g)
  g4. ees'8 ees16( c) c( a) a( g) g( f)
  f4 r8 f' \appoggiatura g32 f16 ees f8 \appoggiatura g32 f16 ees f8
  ees4 r8 c' \appoggiatura f,32 ees16 d ees8 \appoggiatura f32 ees16 d ees8 
  d4 r8 bes' \appoggiatura ees,32 d16 c d8 \appoggiatura ees32 d16 c d8 
  c16 f, c'4 f8 d16 f, d'4 f8
  c16 f, c'4 f8 d4 r8 bes
  f' f f f g f16 ees d c d ees 
  f8 ees16 d c bes c d ees8 d16 c bes a bes c 
  d bes  c a bes4 r2
  ees8 g4 c,8 d f4 bes,8 c ees4 a,8 bes4 r8 f' ees16 d ees8 d16 c d8 c16 bes c8~ c f
  ees16 d ees8 d16 c d8 c16 bes c8 r4
  r r8 f g2~ 
  g8 f16 ees d c d ees f2~
  f8 ees16 d c bes c d ees2~
  ees8 d16 c bes a bes c d d ees f bes,4
  r16 d ees f bes,4 r16 d ees f bes,4 
  r16 d ees f bes,4 r16 f' ees d  c8. bes16
  bes a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes a8 g f4
  bes16 a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes f4 r
  \mark \default
  f'16 bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d 
  d4(\trill c)\breathe c16 f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16 f g8 g,16 a bes8
  a f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f g aes
  % Measure 90
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g a bes
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a' bes4\fermata r r2
  \bar "|."
  
}

first_violin= \new Voice\relative a' {
  \set Staff.instrumentName = #"Violin 1"
  \clef violin
  \tempo "Allegro" 
  bes16\f a bes c d8 ees f4 r16 f g a
  bes( a) g f ees d c bes a8 g f4
  bes16\p a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes f4 r
  f'16\p bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d
  d4\trill\>( c\!)\breathe c16\f f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16( f g8) g,16( a bes8)
  % Measure 10
  a8 f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f( g aes)
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g( a bes)
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a'
  \mark \default 
  bes4 r8 bes,, bes c d bes 
  c d ees c d c d bes 
  c a' f a bes f d bes 
  bes c d bes c d ees c 
  d c d bes c a' f a 
  bes f d bes bes c d bes 
  f' g a g f g a f 
  bes, c d bes c4 c 
  f8 ees d bes bes c d bes 
  f' g a g f g a f
  bes, c d bes c4 c
  f8 g a g f f e e 
  d d c c bes bes a a 
  f' bes, c c f16 e f g a8 bes 
  c4 r16 c d e f e d c bes a g f
  e8 d c4 c'16\p f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8 
  d4 r d16 g, d'4 f8 
  e16 g, e'4 g8 d16 g, d'4 f8
  e4 r e16\f a, e'4 g8
  f16 a, f'4 a8 e16 a, e'4 g8
  f4 r8 f\ff g16 a bes a g f e d
  cis a e'4 g8 f d e cis
  % Measure 40
  \mark \default 
  d4 r r2
  r1
  d,4 d d d 
  a a a a 
  d d bes bes
  a a a a 
  a a d d 
  d d d d 
  g, g c c 
  c c d d 
  d d g, g 
  d' d d d
  g'16\f fis g a bes8 c d4 r8 fis,\p
  a16 fis e d a' fis e d bes'8 g r g
  fis16 d a'4 fis8 g16 d bes'4 g8 
  fis16\f d a'4 fis8 g bes, a fis'
  bes,4 r r2
  r1
  r
  r
  r
  bes,8 c d c bes4 r 
  f'8 g a g f4 r
  bes,8 c d c bes4 r
  c'16 f, c'4 f8 d16 f d4 f8
  c16 f, c'4 f8 d4 r
  r1
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  bes16  a bes c d8 ees f4 r16 f g a
  % Measure 80
  bes a g f ees d c bes a8 g f4
  bes16 a bes c d8 ees f4 r16 f g a
  bes a g f ees d c bes f4 r
  \mark \default
  f'16 bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d 
  d4(\trill c)\breathe c16 f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16f g8 g,16 a bes8
  a f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f g aes
  % Measure 90
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g a bes
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a' bes4\fermata r r2
  \bar "|."
  
}

second_violin= \new Voice\relative a' {
  \set Staff.instrumentName = #"Violin 2"
  \clef violin
  \tempo "Allegro"
  d16 c d ees f8 g a,4 r8 c 
  d4~ d16 d ees f f,2
  d'16 c d ees f8 g a,4 r8 c
  d4~ d16 f ees d d8 c r4
  d8 d16 bes d bes d bes ees8 ees16 bes ees bes ees bes 
  d8 d16 bes d bes d bes ees8 d c bes 
  bes4 a \breathe a8 a16 f a f a f
  bes8 bes16 f bes f bes f a8 a16 f a f a f
  bes d c d f8 d c16 d e8 e,16 f g8
  f a' bes g f4 r
  d16 c d ees f8 g aes16 f d bes aes' f d bes
  aes'8 f4 ees16 d ees bes ees bes bes' g bes g
  e d e f g8 a  bes16 g e c bes' g e c 
  bes'8 g4 f16 e f c f c a' f a f 
  c a c a c a c a bes f bes f bes f bes f 
  a f a f a f a f f8 bes' c, a' 
  bes4 r8 bes,, bes c d bes 
  c d ees c d c d bes 
  c a' f a bes f d bes 
  bes c d bes c d ees c 
  d c d bes c a' f a 
  bes f d bes bes c d bes 
  f' g a g f g a f 
  bes, c d bes c4 c 
  f8 ees d bes bes c d bes 
  f' g a g f g a f
  bes, c d bes c4 c
  f8 g a g f f e e 
  d d c c bes bes a a 
  f' bes, c c f16 e f g a8 bes 
  e,4 r8 g a4~ a16 a bes c
  c,2 a'8 a16 f a f a f 
  bes8 bes16 f bes f bes f a8 a16 f a f a f 
  bes4 r b8 b16 g b g b g 
  c8 c16 g c g c g b8 b16 g b g b g 
  c4 r cis8 cis16 a cis a cis a 
  d8 d16 a d a d a cis8 cis16 a cis a cis a
  d4 r8 d e16 f g a bes a g f 
  e cis g'4 e8 d f g e 
  d4 r r2
  r1
  d,4 d d d 
  a a a a 
  d d bes bes
  a a a a 
  a a d d 
  d d d d 
  g, g c c 
  c c d d 
  d d g, g 
  d' d d d
  bes'16 a bes c d8 ees fis,4 r8 d'
  fis16 a, g fis fis' a, g fis g4 r8 d'
  d16 a fis'4 d8 d16 bes g'4 d8
  d16 a fis'4 d8 bes g fis d' 
  bes4 r r2
  r1
  r
  r
  r
  bes,8 c d c bes4 r 
  f'8 g a g f4 r
  bes,8 c d c bes4 r
  a'8 a16 f a f a f bes8 bes16 f bes f bes f
  a8 a16 f a f a f bes4 r
  r1
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  d16 c d ees f8 g a,4 r8 c 
  d4~ d16 d ees f f,2
  d'16 c d ees f8 g a,4 r8 c
  d4~ d16 f ees d d8 c r4
  d8 d16 bes d bes d bes ees8 ees16 bes ees bes ees bes 
  d8 d16 bes d bes d bes ees8 d c bes 
  bes4 a \breathe a8 a16 f a f a f
  bes8 bes16 f bes f bes f a8 a16 f a f a f
  bes d c d f8 d c16 d e8 e,16 f g8
  f a' bes g f4 r
  d16 c d ees f8 g aes16 f d bes aes' f d bes
  aes'8 f4 ees16 d ees bes ees bes bes' g bes g
  e d e f g8 a  bes16 g e c bes' g e c 
  bes'8 g4 f16 e f c f c a' f a f 
  c a c a c a c a bes f bes f bes f bes f 
  a f a f a f a f f8 bes' c, a' 
  bes4\fermata r r2
  \bar "|."
}

viola= \new Voice\relative f' {
  \set Staff.instrumentName = #"Viola"
  \clef alto
  \tempo "Allegro"
  f4. ees8 c4 r8 a'
  f4. d8 c2
  f4. ees8 c4 r8 a'
  f d bes bes' bes a r4
  bes,4 bes bes bes 
  bes bes bes8 c d ees
  f g a g f4 f
  f f f f
  f f8 bes g4 g8 e
  c c d c a' g f ees 
  f4 f d d
  d d bes bes8 g'
  g4 g g g 
  e8 e e e c4 c 
  a' a f f 
  f f d8 f g f 
  d4 r8 bes bes c d bes
  c d ees c d c d bes
  c a' f a bes f d bes
  bes c d bes c d ees c 
  d c d bes c a' f a 
  bes f d bes bes c d bes 
  f' g a g f g a f
  bes, c d bes c4 c 
  f8 ees d bes bes c d bes 
  f' g a g f g a f bes, c d bes c4 c
  f8 g a g f f e e 
  d d c c bes bes a a 
  f' bes, c c c4. bes8
  g4 r8 e' c4 c8 bes
  g  e' f g c,4 f
  f f f f 
  f8 d16 ees f8 d g4 g 
  g g g g 
  g8 e16 f g8 e a4 a 
  a a a a 
  a8 f16 g a8 f bes4. bes8
  ees,4 cis a8 a' bes a 
  \mark \default
  f4 r r2
  r1
  d4 d d d
  a a a a
  d d bes bes
  a a a a 
  a a d d 
  d d d d 
  g, g c c 
  c c d d 
  d d g, g 
  d' d d d 
  bes' a8 g a,4 r8 a'
  a4 fis d8 c d bes
  a'4 a bes bes 
  a a8 fis d4 d 
  d r r2
  r1
  r
  r
  r
  bes8 c d c bes4 r 
  f'8 g a g f4 r
  bes,8 c d c bes4 r
  f' f f f 
  f f f r
  r1
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  f4. ees8 c4 r8 a' 
  f4. d8 c2
  f4. ees8 c4 r8 a' 
  f d bes bes' bes a r4
  bes, bes bes bes
  bes bes bes8 c d ees
  f g a g \breathe f4 f
  f f f f
  f f8 bes g4 g8 e 
  c c d c a' g f ees 
  f4 f d d
  d d bes bes8 g'
  g4 g g g 
  e8 e e e c4 c 
  a' a f f 
  f f ees8 f g f ees4\fermata r r2
  
}

bass= \new Voice\relative bes, {
  \set Staff.instrumentName = #"Continuo"
  \clef F
  \tempo "Allegro"
  bes4 a8 g f4 r8 f' 
  bes4 bes, f'8 ees d c 
  bes4 a8 g f4 r8 f'
  bes, c d ees f ees d c 
  bes4 bes bes bes 
  bes bes bes8 c d ees
  f g a g f4 f
  f f f f 
  bes, bes c8 d e c 
  f f bes, c f ees d c 
  bes4 bes bes bes 
  bes8 bes bes bes ees f g ees
  c4 c c c 
  c8 c c c f a g f 
  f4 f f f 
  f f bes,8 bes ees f 
  bes,4 r r2
  r1
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r
  r2 f'4 e8 d 
  c4 r8 c f4 f,
  c'8 c d e f4 f
  f f f f8 ees 
  d bes16 c d8 bes g'4 g
  g g g g8 f 
  e c16 d e8 c a'4 a
  a a a a8 g
  f d16 e f8 d g4. g8
  a a, a a d d g, a 
  d^"Solo" f g4 a cis, 
  d8 f g4 a cis,
  d r r2
  r1
  r
  r
  r
  r
  r
  r
  r
  r
  g4^"Tutti" f8 ees d e fis d 
  d,4 d g8 a bes g
  d'4 d d d 
  d d g8 g, d' d, 
  g4 fis8^"Solo"d g a bes a 
  g4 c8 d g, a bes g
  bes4 b c ees 
  f a, bes d 
  ees g, a a 
  bes r r2
  r1
  r
  f'4^"Tutti" f f f
  f f8 ees d bes16^"Solo" c d8 bes 
  bes c d bes ees4 a,
  d g, c f, 
  bes4. bes8 bes c d bes 
  ees4 a, d g, 
  c f, bes8 c d bes
  f' f f f f f f f 
  f f f f f f f f
  bes, bes bes bes ees ees ees ees
  a, a a a d d d d 
  g, g g g c c c c
  f f f f bes bes a a 
  g g f f ees ees d d 
  c c bes bes bes bes f' f, 
  bes4^"Tutti" a8g f4 r8 f'
  bes4 bes, f'8 e d c 
  bes4 a8 g f4 r8 f' 
  bes, c d ees f ees d c 
  bes4 bes bes bes
  bes bes bes8 c d ees
  f g a g f4 f 
  f f f f
  bes, bes c8 d e c
  f f bes, c f ees d c 
  bes4 bes bes bes 
  bes8 bes bes bes ees f g ees
  c4 c c c 
  c8 c c c f a g f 
  f4 f f f 
  f f bes,8 bes ees f
  bes,4\fermata r r2
  \bar "|."
}

figured_bass= \new FiguredBass {
  \figuremode {
  }
}

\score {
  \new StaffGroup <<
    \new Staff << \global \OboeSolo >>
    %\new Staff << \global \violinSolo >>
    %{
    \new StaffGroup <<
      \new Staff << \global \first_violin >>
      \new Staff << \global \second_violin >>
      \new Staff << \global \viola >>
      \new Staff << \global \bass \figured_bass >>
    >>%}
    
  >>
  \layout { }
  %\midi {}
}