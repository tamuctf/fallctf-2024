use lib 'lib';
use Acme::EyeDrops 'sightly';
print sightly( { Shape       => 'map_world3,map_world2,map_world1',
                 SourceFile  => 'source.pl',
                 Regex       => 0 } );
