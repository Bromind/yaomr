#!/bin/sh
# Author: Martin Vassor
# Description: 
# Creation date: 24-02-2018
# Last modified: sam. 24 févr. 2018 18:21:37 CET
# Known bugs: 

print_help() {
	echo "Usage: $0 file.ly"
}


lilypond $1 
g=${1%.ly}
convert "$g.pdf" "$g.png"

: <<=cut

=pod

=head1 NAME

=head1 SYNOPSIS

=head1 AUTHOR

=cut
