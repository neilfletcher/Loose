# Loose! A Company of Archers

An idle strategy game of the Hundred Years' War, from the Southampton muster to Orléans.

**Play it:** https://neilfletcher.github.io/Loose/  
**Also on itch.io:** https://trooperlooper.itch.io/loose  
**Support it:** https://ko-fi.com/trooperlooper

## How it plays

- **Battles run themselves.** Your company fights stage after stage on a top-down field, even while you're away. Your decisions are who stands in the line, where they stand and how strong they are. The front rank shoots harder but takes the charges; the back rank is safe from all but horsemen.
- **Gather and build.** Food, wood, iron, feathers and arrows come from farms, woodcutters, mines, goose pens and the fletcher. Storage caps make you come back, and the Market sells the overflow. Thirteen buildings unlock as you push deeper.
- **Recruit at the tavern.** Spend writs on recruits of five rarities, from Common levy to four Legendary named archers. There's a pity timer, and duplicate Legendaries gain stars.
- **Every man is a person.** Recruits have names, back stories and traits. Train them with food and silver; damage doubles every 25 levels. Promote them with medals for stars and higher level caps.
- **Orders.** Daily rations, rotating quests from the King, and expeditions that send spare men away for hours and bring back resources, stories and new habits.
- **Camp news.** Choices with consequences between battles.
- **Legacy.** From stage 40, end the campaign for glory and spend it on permanent upgrades. The next campaign starts from scratch but goes much further.
- **Offline progress.** Four hours by default, more with Legacy and research.
- **Gear.** Bows, arrowheads, armour and charms in five rarities drop from bosses, set pieces and expeditions. Spare gear breaks down into iron, feathers and medals.
- **Support troops.** Billmen hold the road, pavise-bearers shelter the line, and a trebuchet lobs stones into the thickest crowd.
- **Set pieces.** Every 25 stages, a historical battle with its own rules: the mud, the night raid on the baggage, the flux, rain on the strings, the great charge, and the crossbows under the walls.
- **The men's stories.** Archers who stand side by side become friends or enemies, earn nicknames for what they've done, and can fall for good in boss fights. The Company Chronicle and the Roll of Honour keep the record.
- **Research.** A permanent tree across Archery, Logistics and Command, paid for in parchment from the Scriptorium, with choices that rule each other out.
- **The Order of the Garter.** A second prestige layer: after ten campaigns, give up your whole Legacy for Garter stars and far bigger rewards.
- **The Codex.** Permanent bonuses for enemies killed, men recruited, zones conquered and set pieces won.
- **Accounts.** Sign in with Google to save to the cloud and carry on from any device, or move your game with a save code.
- **Installable.** Add it to your home screen as an app, with notifications when expeditions return, research finishes or stores fill.
- **A guided start.** Seven short steps teach the basics and open the tabs one at a time.
- **Twelve Legendaries.** Each has its own special, with a featured Legendary every week who makes up half of all Legendary recruits.
- **Weekly events.** A special campaign each week with its own rules, milestone rewards and a token shop, including that week's featured Legendary.
- **The King's League.** A weekly leaderboard for signed-in captains, ranked by furthest stage.
- **Music.** A medieval loop that picks up pace for bosses and set pieces.
- **Your company.** Name your captain, company and men, and choose your banner colours. Portraits gain plumes and gilt as men are promoted.
- **Admin.** `admin.html` shows anonymous play figures from players who agreed to share them: where people stop, prestige, building and research choices.
- **Privacy.** `privacy.html` is the privacy notice. Play stats and Google Analytics only run after the player says yes (asked after 45 seconds of play; Settings, Privacy to change).

Twelve zones with their own enemy mixes (swarm, armoured, cavalry, crossbows) loop with rising difficulty, and there's a boss every ten stages.

## Tech

A single `index.html`: vanilla JS, canvas rendering and Web Audio, plus a service worker and web app manifest. Progress saves in localStorage and, when signed in, to Firestore (Firebase project `until-crispins-day`, collections `loose_saves`, `loose_players` and `loose_league`). No build step.

## Portal copies and adverts (2.27)

`python3 tools/build-portal.py crazygames` writes `dist/crazygames/` and a zip to upload to a game site. A portal copy has no sign-in, no Firebase, no Analytics, no play stats, no gifts, no update prompt and no outside links; saves stay in the browser. `?portal=name` on the live site behaves the same way, for testing.

Rewarded adverts are optional, capped per day and only offered from stage 10 where an advert provider exists: double offline silver and materials (3 a day), hurry a building by 30 minutes (3), a free writ (1), swap a daily order (2). `?adtest=1` adds a fake three-second advert for testing. A portal's SDK plugs in as `adProv = {name, show: placement => Promise<boolean>}`.

The Ko-fi supporter card in Settings appears once `KOFI` is set at the top of the script. Supporters unlock two extra banners, on trust.
