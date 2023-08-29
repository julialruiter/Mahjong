# Class: Table
## wind:  str/int (from set of 4), default: East
## number players: from set [3, 4]
## player ID/wind assignment
## tile pool/wall:  set of all 134 tiles (or should it be an ordered list?)
## dead wall: set of 14 tiles, taken from tile pool.  Need to decide if ordering/placement matters
## dora indicator: need to decide if placement matters:  either tile location in dead wall or actual value
## dora bonus:  determined by indicator, equals dora value or dora value +1 (default) depending on game mechanic
## remaining tile count:  134 minus dead wall minus drawn
## revealed tiles:  set of all revealed tiles (keep private? and/or make join of player sets)
## player riichi status?

## f(n):  update draw pile (remove from set/pop off list)
## f(n):  setup game (walls, winds, etc)
## f(n):  toggle in progress state (or make "has won" flag?) ==> else move to main.py "while" loop 
## f(n):  flip dora


## NOTE:  for logic, is it better to have a dict of all cards and track number exposed (per player) for calculating draw percent?
## if so, function: show exposed tiles (from player perspective) may be helpful

__________________________________________________________________
# Class: Tile
## Suit:  str or int ==> should "honor" be considered a suit for this purpose?
## Value: [1-9] for number tiles, blank(?) for honor?
## Red tile:  bool (or string):  only applies to 3 tiles in game
## Representation: ??

## NOTE: need to decide on represntation:  Should "Character 5 (red)" be ['character',5,'red'],'C5!', [1,5,1], ...?
## individual components may make extracting parts for logic easier (ex:  waiting on a particulr 6, checking if cuit commonly discarded,...)

__________________________________________________________________
#Class:  Player ==> split out into hand class and agent class?
## Current hand:  set of tiles (join open and closed hand?)
## Open hand
## Closed hand
## Drawn tile:
## Waiting tiles: (may also serve as "danger tiles" to opponents (if known) ==> create "open" waiting tiles subset?)
## Discards: (order matters)
## Riichi bet:  bool (public)
## Skill level:  (future implementation)
## Tenpai:  bool (private)

## f(n):  draw tile
## f(n):  discard tile
## f(n):  call pon/kan/chi

## NOTE:  weight of waiting/discard tile choices should rest in AI class

__________________________________________________________________
# Class:  Evaluation ==> will be split up to other classes since some are shared resources
## safe tiles
## win probability
## tile draw probability
## winning conditon acheived/pending

__________________________________________________________________
# Class: Scoring
## list of winning hands (and points)
## account for dealer
## bonuses (dora, etc)

