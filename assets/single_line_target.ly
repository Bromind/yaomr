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
}

\score {
  \new Staff << \global \violinSolo >>
  \layout { }
  \midi {}
}
