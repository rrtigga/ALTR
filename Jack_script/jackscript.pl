#!/usr/bin/perl

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Script reads output from Netapp df command
# and reports "used" T1, T3 storage tiering information as well as
# Site, Dept, and aggr_type.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while (<>)
{
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# process line, add blank space to certain fields
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s/GB/ GB/g;
s/TB/ TB/g;
s/%/ %/g;
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# split fields
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@F = split;
$used_GB = $F[3];
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# process Filer line
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if (/Filer:/) {
$filer_name = $F[1];
$filer_name =~ /(\w\w)-(\w\w\w\w\w)/;
$site=$1;
$dept=$2;
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# process aggr line
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if (/sas/i) {
#T1
$aggr_name = $F[0];
$aggr_name =~ /(\w\w\w\w)/;
$aggr_type = $1;
print "$site,$dept,$filer_name,$used_GB,0,$aggr_type\t$_";
}
elsif (/sata/i) {
#T3
$aggr_name = $F[0];
$aggr_name =~ /(\w\w\w\w)/;
$aggr_type = $1;
print "$site,$dept,$filer_name,0,$used_GB,$aggr_type\t$_";
}
elsif (/aggr/) { #note: case sensitive here ...
#T1? most likely
$aggr_name = $F[0];
$aggr_name =~ /(\w\w\w\w)/;
$aggr_type = $1;
print "$site,$dept,$filer_name,$used_GB,0,$aggr_type\t$_";
}
elsif (/loaner/i) { #note: case sensitive here ...
#skip loaner
print "0,0,0,0,0\t$_";
}
else {
#skip everything else
print "0,0,0,0,0\t$_";
}
}