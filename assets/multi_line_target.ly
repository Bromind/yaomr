\version "2.18.2"

\header {
}


global= {
  \key c \major
  \time 4/4
}

violinSolo= \new Voice \relative a' {
  \clef violin
  b16 a b c d8 e f4 f
  g, a b a
  c8 d c4 a b
  e f e d 
  c g a a

}

\score {
  \new Staff << \global \violinSolo >>
  \layout { }
  \midi {}
}
