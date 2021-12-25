#!/usr/bin/perl -w
use strict;

my $input1 = <<EOF
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -2
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
EOF
;

##########
my $input = $input1;

my(@p, @q, @r);
my $big = 0;

while ($input =~ /\G.*?div z (-?\d+)\s*add x (-?\d+).*?add y w.*?add y (-?\d+)/sg) {
	push @p, $1;
	push @q, $2;
	push @r, $3;
}
print scalar(@p), ": ", join(",", @p), "\n";
print scalar(@q), ": ", join(",", @q), "\n";
print scalar(@r), ": ", join(",", @r), "\n";

do { ++$big if $_ >= 26 } for @p;
print "big: $big\n";

sub wfromx {
	my($z, $i) = @_;
	return ($z % 26) + $q[$i];
}

sub calc {
	my($z, $w, $x, $i) = @_;
	my $y = 25 * $x + 1;
	my $new = int($z / $p[$i]) * $y + ($w + $r[$i]) * $x;
	# print "$z, $w, $x, $i -> $new\n";
	return $new;
}

sub solve {
	my($z, $i, $b) = @_;
	unless ($i < @p) {
		return "" if $z == 0;
		return;
	}
	my($new, $w, $x, $s);
	my $wfx = wfromx($z, $i);
	for ($w = 9; $w > 0; --$w) {
		$x = ($w == $wfx) ? 0 : 1;
		next if $b < $x;
		$new = calc($z, $w, $x, $i);
		$s = solve($new, $i + 1, $b - $x);
		return $w . $s if defined($s);
	}
	return;
}

my $solution = solve(0, 0, $big);
print "$solution\n";
