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
  bes16 a bes c d8 ees f4 r16 f g a
  bes a g f ees d c bes a8 g f4
  bes16 a bes c d8 ees f4 r16 f g a 
  bes a g f ees d c bes f4 r
  f'16 bes, f'4 bes8 g16 bes, g'4 bes8
  f16 bes, f'4 bes8 g f ees d
  d4 c c16 f, c'4 f8
  d16 f, d'4 f8 c16 f, c'4 f8
  d16 bes a bes bes'8 g e16 f g8 g,16 a bes8
  % Measure 10
  a8 f' g e f4 r
  bes,16 a bes c d8 ees f4 r16 f g aes
  bes,8 aes'4 g16 f g f ees8 r4
  c16 bes c d e8 f g4 r16 g a bes
  c,8 bes'4 a16 g a g f8 r f
  ees16 c a'4 ees8 d16 bes bes'4 d,8
  c16 f, ees'4 c8 d bes' c, a'
  bes4 r r2
  r1
  r2 r4 r8 bes,
  \bar "|."
}

\score {
  \new Staff << \global \violinSolo >>
  \layout { }
  %\midi {}
}
