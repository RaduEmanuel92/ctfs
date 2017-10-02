#!/usr/bin/perl

use Digest::MD4 "md4_hex";

my $username = "admin";
my $pass = "acasa";
print md4_hex($pass) . lc($username) . "\n";
print md4_hex( md4_hex($pass) . lc($username) ) . "\n";