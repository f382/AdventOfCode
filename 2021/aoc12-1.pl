#!/usr/bin/perl -w
use strict;

my @input = qw(
ex-NL
ex-um
ql-wv
VF-fo
VF-ql
start-VF
end-tg
wv-ZQ
wv-um
NL-start
lx-ex
ex-wv
ex-fo
sb-start
um-end
fo-ql
NL-sb
NL-fo
tg-NL
VF-sb
fo-wv
ex-VF
ql-sb
end-wv
);

my %graph = ();

foreach my $line (@input) {
	die unless $line =~ /^(\w+)-(\w+)$/;
	push @{$graph{$1}}, $2;
	push @{$graph{$2}}, $1;
}

my $paths = 0;

sub visit {
	my($node, %visited) = @_;
	print "-> $node\n";
	if ($node =~ /^[a-z]+$/ and $visited{$node}) {
		print "!\n";
		return 0;
	}
	++$visited{$node};
	if ($node eq 'end') {
		print "#\n";
		return 1;
	}
	my $result = 0;
	foreach my $neigh (@{$graph{$node}}) {
		next if $neigh eq 'start';
		$result += visit($neigh, %visited);
	}
	print "<- $node \n";
	return $result;
}

my $count = visit('start', ());

print "$count\n";
