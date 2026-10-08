# -*- coding: utf-8 -*-
"""
Builder for Chapter 5 of Wang Mingdao's 'The True Meaning of Being Born Again'
(《重生真意》第五章：五、得了重生的人还能犯罪吗？)
"""
import json

def get_ch5_translations():
    # Exactly 80 English translations corresponding to the 80 paragraphs
    translations = [
        # 1
        "Chapter 5: Can a Person Who Is Born Again Still Sin?",
        # 2
        "The question we are now about to investigate is by no means: \"May a person who is born again go on sinning?\" To this question the Holy Scriptures have already provided an emphatic and crystalline answer: \"By no means!\" (cf. Romans 6:1–2).",
        # 3
        "Nor is our question: \"Does a person who is born again desire to sin?\" No one who has truly been born again cherishes a desire to sin. If a person actually desires to sin, that very desire proves that he has never been born again. Still less is our question: \"Ought a person who is born again to sin?\" Such a question is utterly unthinkable; not a single person on earth ought ever to sin.",
        # 4
        "Our question is strictly this: \"Can a person who is born again still sin?\" In other words: \"Does the possibility of sinning still remain in one who has been born again?\"",
        # 5
        "Because many devout believers do not clearly grasp this truth, they bring upon themselves immense and needless fear, sorrow, despair, and anguish. These are genuine believers who have truly trusted in Christ and experienced the new birth. When they first repented and believed, they grieved and wept over their sins with such brokenness, loathing sin to the uttermost, that they resolved to sever all ties with iniquity for the rest of their days. They determined never to sin again, imagining that since they hated sin so intensely and had resolved so firmly to forsake it, they would surely be able to live the rest of their lives without ever sinning again. To their dismay, after a season, they actually fell into sin—and in some cases, even stumbled into what human eyes regard as grievous sins! In that dreadful hour, they began to doubt whether they were truly born again, asking: \"If I am truly regenerate, how could I possibly have sinned again?\"",
        # 6
        "If they have listened to preachers who proclaim, \"A born-again person can never sin again,\" they become all the more convinced that they have never experienced the new birth. Imagining that they are still unregenerate (when in truth they have already been born again), they naturally set out once more to seek the experience of regeneration. They repent anew, they believe anew, and they humble themselves before God in deep contrition for their sins. They think to themselves, \"Now at last I am born again, and from now on I will never sin again!\" But alas, after a while, they fall into sin once more. At this point, they are completely bewildered. They wonder in agony: \"Am I born again or not? If I say no, I have truly tasted the undeniable experience of the new birth; if I say yes, how is it that I am still capable of sinning?\" When a believer reaches such a crisis, he is on the brink of despair and ruin, and may even end up doubting the very faith he has embraced.",
        # 7
        "Still other believers fall into an even more perilous delusion. Having committed a sin unawares after being born again, they conclude that they are eternally damned! They imagine that the sin they have now committed can never again be forgiven. They suppose that they have sinned willfully with their eyes wide open, and that they have committed the blasphemy against the Holy Spirit (though what blasphemy against the Holy Spirit actually means they have not the faintest idea!). They assume that if a regenerate person sins again, he is forever beyond the reach of divine mercy. This fatal misconception has tormented countless believers. They have not been cast off by God at all, yet believing themselves utterly abandoned, they spend their days in trembling, despair, agony, and gloom. Being trapped in so pitiable and wretched a state, they are naturally incapacitated from helping or guiding others.",
        # 8
        "How do the Holy Scriptures answer this question?",
        # 9
        "\"If we say we have no sin, we deceive ourselves, and the truth is not in us. If we confess our sins, He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.\" (1 John 1:8–9)",
        # 10
        "Who are the \"we\" spoken of in this passage? This epistle of John was written not to the unregenerate world, but to those who were already born again. Furthermore, he does not say \"you,\" but \"we\"—thereby explicitly including himself! Surely no one would dare to assert that the aged Apostle John was an unregenerate man! Yet he writes: \"If we say we have no sin, we deceive ourselves, and the truth is not in us.\" If a person who is born again is incapable of committing sin, how are these words to be explained?",
        # 11
        "Proceeding further, he reveals the divine remedy for cleansing: \"If we confess our sins, He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.\" Here John tells us that although we recognize sin within ourselves, we need not plunge into despair or terror; if only we confess our sins, we will surely receive forgiveness and cleansing.",
        # 12
        "Simultaneously, we discern from this verse that a person who is born again can still sin. Precisely because a regenerate person is capable of sinning, he stands in need of confessing his sins so that he may receive forgiveness and cleansing. Let us read on to the next words penned by John:",
        # 13
        "\"My little children, I am writing these things to you so that you may not sin. But if anyone does sin, we have an advocate with the Father, Jesus Christ the righteous. He is the propitiation for our sins, and not for ours only but also for the sins of the whole world.\" (1 John 2:1–2)",
        # 14
        "These words likewise are addressed to those who are already born again. John declares that he writes these things to them so that they may not sin. That it was necessary to write this exhortation to them proves conclusively that they are capable of sinning. It is precisely because they can sin that John writes to them—to help them, warn them, and keep them from sinning.",
        # 15
        "Yet suppose someone should unhappily fall into sin—what then? Does John go on to say: \"If anyone sins, this proves he does not belong to God and has never been born again\"? Or does he say: \"If anyone sins, he has sinned presumptuously and must abandon all hope of forgiveness\"? Or does he say: \"If anyone sins, God will revoke his salvation and strip him of his sonship\"? Nothing of the kind! John never uttered such words. Those notions were invented by subsequent commentators. What John actually declared is this:",
        # 16
        "\"If anyone does sin, we have an advocate with the Father, Jesus Christ the righteous. He is the propitiation for our sins...\"",
        # 17
        "Oh, what precious, priceless words! How mightily these words succor those believers who have been wounded and battered by sin! How sweetly they console them, preserving them from despair and utter ruin! If every child of God kept these words clearly in remembrance, how much needless anguish, fear, sorrow, and despair would be instantly banished! How many sin-wounded saints would immediately find healing!",
        # 18
        "Yet some might imagine that this biblical teaching is dangerous, fearing that such a promise will embolden believers to sin with brazen impunity. They think we ought to warn believers with ferocious severity, telling them that if a saved person sins again, he is crucifying the Son of God afresh and has no hope of forgiveness—supposing that only such terror will keep believers from sinning. They fear that if we proclaim that a saved person who sins can still be forgiven, multitudes will sin with reckless abandon. What a terrible prospect that would be!",
        # 19
        "Such reasoning arises purely from an ignorance of biblical truth. If a believer truly understands the doctrine of regeneration and has walked with the Lord in personal experience, he will never utter such words nor harbor such groundless fears. Far from deeming this passage harmful, he will pour out his heart in boundless thanksgiving and praise to God for this very Scripture!",
        # 20
        "Allow me to use an illustration: On one occasion, I was staying at the home of a friend. One morning while shaving with a razor, my hand slipped and I cut my face. My friend's home was well stocked with medical supplies. The moment he saw that I had cut myself, he immediately brought out a bottle of antiseptic ointment, applied some to my wound, and gave the bottle to me as a gift. He told me that whenever I cut my face or my hand, I could apply this ointment at once to prevent infectious poison from entering the wound and causing serious danger.",
        # 21
        "My friend further promised that whenever this bottle was exhausted, he would gladly give me another. Because I had received so invaluable a remedy to protect me against the danger of wound infection, I was deeply grateful to my friend.",
        # 22
        "Later, upon returning to my room, I opened the bottle and saw that it contained an ample supply of ointment—enough, I estimated, to treat dozens of cuts. Thereupon, did I pick up my razor and deliberately slash my face left and right, carving gash after gash across my cheeks, and then dab on the ointment to match the number of cuts, crying out: \"How marvelous! Now that I have this wonderful wound ointment, I can slash my face and cut my hands whenever I please without the slightest fear!\"?",
        # 23
        "Tell me: if I had acted in such a manner, what would anyone who saw me have said? They would have pronounced without hesitation that I had gone stark raving mad! But I would never do such a thing; I could never do such a thing! The wound ointment is a precious and beneficial gift; I received it from my friend with profound gratitude, and I preserved it carefully against the event that my hand might slip and cut my skin. But under no circumstances would I ever deliberately slash my own flesh simply because I possessed the ointment! To cut one's own flesh inflicts severe injury and excruciating pain; who in his right mind would ever do such a thing unless he were insane?",
        # 24
        "The words of 1 John 2:1–2 are precisely like a bottle of divine wound ointment given by God to His children. Seeing that through carelessness they sometimes suffer injury—that is, commit sin—and fearing lest they contract deadly infection through their wound—that is, fall into despair and spiritual collapse—He places this bottle of healing balm into their hands, bidding them apply it immediately whenever they are wounded.",
        # 25
        "Wound ointment is intended for those who accidentally cut their skin, but no sane person deliberately slashes his flesh because he possesses ointment, for cutting his own flesh causes agony. This gracious word of God is provided for believers when through weakness they stumble into sin; but no true believer will ever deliberately sin simply because this gracious promise exists, for committing sin is the most excruciating agony to a born-again soul—infinitely more painful than cutting his physical flesh!",
        # 26
        "I desire to commend this bottle of spiritual healing balm to all who believe on the Lord. I have no fear that they will run into sin upon hearing this truth, for I know full well that one who is truly born again will never deliberately practice sin. Perhaps there may be certain church members (notice I call them church members, not Christians) who have never genuinely repented and believed, and have never experienced the new birth, who might presume upon this scripture to sin with impunity. But this gives us no cause for concern: those who are unregenerate love sin in any case; even without this passage of Scripture, would they commit one sin the less?",
        # 27
        "God's promises are prepared exclusively for His children (those who are truly born again). If counterfeit believers who have never been born again presume to misuse God's Word, that is beyond our power to prevent.",
        # 28
        "When a believer sins, it is exactly like a person suffering an accidental injury. No one desires to be injured, yet no one can entirely avoid suffering wounds. We ought to instruct our children to be vigilant so that they do not hurt themselves; at the same time, we must prepare medical supplies for treating wounds so that they will not panic when an accidental injury occurs. We can warn them of the pain and peril of wounds so that they exercise caution and guard themselves against injury. But we must never tell them that the moment a person is scratched or cut, he will instantly die from the wound!",
        # 29
        "If we imagine that we must terrorize our students and children in this manner to keep them from hurting themselves, then one day, when they sustain some minor, non-fatal scratch, the child will be driven into a nervous breakdown through sheer terror! What an utterly foolish and disastrous pedagogy that would be!",
        # 30
        "Those who are genuinely born again never desire to sin; yet they can scarcely avoid stumbling at times. Our Heavenly Father, who is infinite in wisdom and love, on the one hand warns us in the Scriptures not to sin, setting before us all the ruinous fruits of iniquity; and on the other hand, He has prepared emergency medicine for us, so that when we accidentally stumble into sin, we may apply it immediately and be preserved from falling into still greater peril.",
        # 31
        "Alas, from what source so many ignorant believers have imbibed such doctrine, I do not know—insisting that if a believer sins after being born again, he can never be forgiven and must forfeit the salvation and eternal life he received! In truth, the inherent consequence of a believer's stumble is not fatal (though sin certainly brings great chastisement and sorrow); yet this false doctrine strikes such terror into the hearts of believers who stumble accidentally that their souls fall severely sick. Some take months and years to recover, while others remain spiritually paralyzed for the rest of their lives. What a heartbreaking tragedy!",
        # 32
        "Let us now turn from the First Epistle of John and read several passages from the First Epistle to the Corinthians:",
        # 33
        "\"Paul, called by the will of God to be an apostle of Christ Jesus, and our brother Sosthenes, To the church of God that is in Corinth, to those sanctified in Christ Jesus, called to be saints together with all those who in every place call upon the name of our Lord Jesus Christ, both their Lord and ours.\" (1 Corinthians 1:1–2)",
        # 34
        "\"For you are still of the flesh. For while there is jealousy and strife among you, are you not of the flesh and behaving only in a human way?\" (1 Corinthians 3:3)",
        # 35
        "\"It is actually reported that there is sexual immorality among you, and of a kind that is not tolerated even among pagans, for a man has his father's wife. And you are arrogant! Ought you not rather to mourn? Let him who has done this be removed from among you.\" (1 Corinthians 5:1–2)",
        # 36
        "\"When one of you has a grievance against another, does he dare go to law before the unrighteous instead of the saints?... but brother goes to law against brother, and that before unbelievers? To have lawsuits at all with one another is already a defeat for you. Why not rather suffer wrong? Why not rather be defrauded? But you yourselves wrong and defraud—even your own brothers!\" (1 Corinthians 6:1, 6–8)",
        # 37
        "\"Let a person examine himself, then, and so eat of the bread and drink of the cup. For anyone who eats and drinks without discerning the body eats and drinks judgment on himself. That is why many of you are weak and ill, and some have died [literally: fallen asleep].\" (1 Corinthians 11:28–30)",
        # 38
        "Let me ask: Were the Corinthian believers born again? At the very opening of his epistle, Paul addresses them as those \"sanctified in Christ Jesus, called to be saints.\" Can we say that those who are sanctified in Christ Jesus are unregenerate? Can an unregenerate person ever be called a \"saint\"?",
        # 39
        "From the words penned by Paul, it is abundantly clear that the Corinthian believers were truly born again. Yet in this very epistle, we find among these believers \"jealousy and strife,\" \"incestuous immorality,\" \"quarrels and lawsuits,\" \"brother dragging brother to court before pagan judges,\" \"defrauding and wronging their own brethren,\" and \"eating and drinking judgment to themselves at the Lord's Table.\" These undeniable facts demonstrate with absolute clarity that those who are born again can still commit sin—and at times, even very grievous sins!",
        # 40
        "Let us read several passages from yet another epistle:",
        # 41
        "\"Paul, an apostle of Christ Jesus by the will of God, To the saints who are in Ephesus, and are faithful in Christ Jesus.\" (Ephesians 1:1)",
        # 42
        "\"Therefore, having put away falsehood, let each one of you speak the truth with his neighbor, for we are members one of another. Be angry and do not sin; do not let the sun go down on your anger, and give no opportunity to the devil. Let the thief no longer steal, but rather let him labor, doing honest work with his own hands, so that he may have something to share with anyone in need. Let no corrupting talk come out of your mouths, but only such as is good for building up, as fits the occasion, that it may give grace to those who hear. And do not grieve the Holy Spirit of God, by whom you were sealed for the day of redemption. Let all bitterness and wrath and anger and clamor and slander be put away from you, along with all malice. Be kind to one another, tenderhearted, forgiving one another, as God in Christ forgave you.\" (Ephesians 4:25–32)",
        # 43
        "Paul designates the Ephesian believers as \"saints\" and \"faithful in Christ Jesus\"—conclusive evidence that they were not only born again, but had attained a high degree of spiritual maturity. Yet it was to these very believers that Paul addressed the extended exhortation quoted above! He urges them: \"Put away falsehood, let each one speak the truth with his neighbor,\" \"Be angry and do not sin,\" \"Give no opportunity to the devil,\" \"Let the thief no longer steal,\" \"Let no corrupting talk come out of your mouths,\" and \"Do not grieve the Holy Spirit of God.\" He further exhorts them to put away \"all bitterness, wrath, anger, clamor, slander, and malice.\"",
        # 44
        "If a person who is born again were incapable of committing sin, would not Paul's lengthy exhortation be rendered utterly nonsensical?",
        # 45
        "We never need to admonish a mute child: \"Do not tell lies; do not use profanity,\" for a mute cannot speak, and therefore cannot utter lies or curses. Nor do we need to warn a blind man: \"Do not read lewd novels or watch corrupting films,\" for a blind man can see nothing, and is incapable of reading novels or watching films. If a born-again person were incapable of sinning, would not Paul's earnest admonitions be just as meaningless as commanding a mute not to swear, or ordering a blind man not to gaze at lustful images?",
        # 46
        "And are such exhortations found only in Ephesians? Are they not scattered abundantly throughout all the Epistles? Not a single epistle written by the Apostles was addressed to the unregenerate world. If born-again believers could not commit sin, would not all these apostolic exhortations be reduced to useless, empty babble?",
        # 47
        "To say nothing of ordinary believers, consider Timothy: he was Paul's most trusted fellow-worker, whom Paul affectionately addressed as his \"beloved son.\" Yet to so holy and faithful a servant of God, Paul still gave this solemn charge: \"Flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.\" (2 Timothy 2:22)",
        # 48
        "If even Timothy needed to be warned to \"flee youthful passions,\" does not the truth that a regenerate person can still sin shine forth with dazzling clarity?",
        # 49
        "Let us now examine a passage recounting Paul's own personal experience:",
        # 50
        "\"For we know that the law is spiritual, but I am of the flesh, sold under sin. For I do not understand my own actions. For I do not do what I want, but I do the very thing I hate. Now if I do what I do not want, I agree with the law, that it is good. So now it is no longer I who do it, but sin that dwells within me. For I know that nothing good dwells in me, that is, in my flesh. For I have the desire to do what is right, but not the ability to carry it out. For I do not do the good I want, but the evil I do not want is what I keep on doing. Now if I do what I do not want, it is no longer I who do it, but sin that dwells within me. So I find it to be a law that when I want to do right, evil lies close at hand. For I delight in the law of God, in my inner being, but I see in my members another law waging war against the law of my mind and making me captive to the law of sin that dwells in my members. Wretched man that I am! Who will deliver me from this body of death? Thanks be to God through Jesus Christ our Lord! So then, I myself serve the law of God with my mind, but with my flesh I serve the law of sin.\" (Romans 7:14–25)",
        # 51
        "Undoubtedly, this passage recounts the intense warfare experienced by Paul after he was born again. He was already regenerate; he possessed a new man within. That inner man, born of God, delighted in the law of God: \"For I delight in the law of God, in my inner being.\" But at the same time, he possessed an old man—the flesh. The old man was contrary to the law of God, and continually dragged him into captivity to the law of sin, plunging him into agonizing distress.",
        # 52
        "How many genuinely born-again believers can echo Paul's words from the depths of their souls! They have experienced this very warfare, suffered these very defeats, and tasted this very agony. Many among them, failing to understand that this is the fierce conflict between the new man and the old, mistakenly concluded that they were not born again at all, and thus fell into despair.",
        # 53
        "An unregenerate person does not delight in the law of God; nor does the law of sin need to take him captive in conflict, for he is already entirely enslaved under the dominion of sin without resistance! Every single person who has been born again has passed through this spiritual warfare. Many regenerate souls have long struggled under this bitter affliction, crying out with Paul: \"Wretched man that I am! Who will deliver me from this body of death?\"",
        # 54
        "There is, however, a passage of Scripture that is frequently misunderstood and cited as supposed proof that a born-again person cannot sin:",
        # 55
        "\"Whoever makes a practice of sinning is of the devil, for the devil has been sinning from the beginning. The reason the Son of God appeared was to destroy the works of the devil. No one born of God makes a practice of sinning, for God's seed abides in him; and he cannot keep on sinning, because he has been born of God.\" (1 John 3:8–9)",
        # 56
        "Some cite this passage and say: \"Does it not plainly state that 'no one born of God commits sin'? And does it not add: 'he cannot sin'?\" If so, how astonishing this would be! Throughout all the scriptures we have just examined, we have seen that a born-again person can indeed commit sin; how then can John declare here that \"he cannot sin\"? Is there a contradiction within the Scriptures? God forbid!",
        # 57
        "\"No one born of God commits sin,\" and \"he cannot sin\"—this is absolute, unshakeable truth! God does not commit sin; therefore, that which is born of God does not commit sin. I believe this without a shadow of doubt. But we must ask: What is that which is born of God? Does it refer to our visible, outer body? By no means! Our outer body was born of our parents; it is \"the outer man.\" That which is born of God is \"the inner man\" residing within us.",
        # 58
        "When a person is born again, his outer man does not drop dead; he remains right there. But within him there is now added an \"inner man\" brought forth by God. For two individuals of completely opposite natures to dwell under one roof is indeed a troublesome situation! They will inevitably engage in perpetual conflict.",
        # 59
        "A born-again person possesses two distinct beings: one is outer, and one is inner. The outer man is born of the flesh—polluted and loving sin; the inner man is born of the Holy Spirit—holy and abhorring sin. Precisely for this reason, the moment a person is born again, the curtain rises on an intense, relentless civil war within his soul: \"For the desires of the flesh are against the Spirit, and the desires of the Spirit are against the flesh, for these are opposed to each other, to keep you from doing the things you want to do.\" (Galatians 5:17).",
        # 60
        "Many who are genuinely born again, because they do not comprehend this profound truth, sink into a pit of doubt and despair. When they first repented and believed, they mourned over their sins with such grief, burning all their bridges behind them to sever ties with iniquity forever. They assumed that having hated sin so fiercely and having embraced Christ so wholeheartedly, they would never stumble again. Yet after a season, they find themselves falling into sin once more, and when they sin, their agony is beyond words. Thereupon, they begin to question: \"Was my repentance genuine? Did I truly receive the new birth? If I am born again, why do I still commit sin?\"",
        # 61
        "If we understand this conflict between the new man and the old, we will realize that the presence of this fierce warfare within a believer, far from proving that he is unregenerate, serves as the most powerful proof that he is truly born again!",
        # 62
        "When they suffer painful defeat, it is simply because their \"inner man\" is still weak and has not yet gained the strength to overcome the \"outer man.\" Having already been born again, they ought not to question the reality of their regeneration; what they need now is to pray with the Apostle that God, \"according to the riches of His glory, may grant them to be strengthened with power through His Spirit in the inner man\" (Ephesians 3:16).",
        # 63
        "Some may ask: \"If a born-again person can still sin, and at times even repeatedly stumble into sin without being able to extricate himself immediately, is he not completely identical to the unregenerate?\" To this question I answer: Emphatically no! The unregenerate person and the born-again person remain worlds apart!",
        # 64
        "The unregenerate person not only sins, but loves to sin! Living in sin brings him no pain; on the contrary, he counts it his delight and chooses to remain in it. The born-again person may also stumble into sin, but he despises sin! He does not desire to sin, yet he finds himself caught unawares; and the moment he sins, his soul is plunged into intolerable anguish, feeling as though he has swallowed poison, and he cannot rest until he has wept bitterly before God, confessed his transgression, and received cleansing.",
        # 65
        "We have all observed sheep and pigs. Between these two domestic animals there is a glaring, fundamental distinction of nature: the former loves cleanliness, while the latter delights in filth. Because the sheep's innate nature loves cleanliness, it seeks clean pasture, drinks clear water, and keeps its fleece white and pure.",
        # 66
        "Although the sheep loves cleanliness, if it is not careful while walking, it may stumble into a muddy ditch where pigs wallow, so that its fleece becomes spattered and smeared with foul mud. A casual onlooker from a distance might even mistake it for a pig.",
        # 67
        "Nevertheless, a sheep remains a sheep! We can never declare that because it has fallen into a mud hole and is covered with slime, it has become a pig. For although it has fallen into the mire, it detests that place; although covered with mud, it bleats in distress, strains every muscle to scramble out of the ditch, and shakes the filth from its wool. The moment it regains dry ground, it runs away from the mud and never voluntarily leaps back in.",
        # 68
        "With the pig, however, it is entirely the opposite! The pig loves the mud hole. It roams about searching for filthy ditches, and the moment it finds one, it plunges straight in, wallows in the stench, slurps up the foul water, eats the refuse, and contentedly falls asleep in the mire! Even if you drag a pig out of the ditch, scrub it with fragrant soap, wash it with clean water, tie a red ribbon around its neck, and release it—in the twinkling of an eye it will gallop straight back into the slough of mud and wallow all over again!",
        # 69
        "Here lies the immense, unbridgeable gulf between the regenerate and the unregenerate! A born-again person is like a sheep: he possesses the divine nature of God, and therefore loves purity and holiness. However, dwelling in this fallen, sinful world full of pitfalls and snares, if he grows careless, his feet will slip into the muddy ditch of sin. When he falls, he suffers intense agony, bleats in sorrow to his Shepherd, and struggles to get out; having been cleansed, he exercises vigilance never to fall into that ditch again.",
        # 70
        "In former years, when I did not understand these truths, I naively assumed that every churchgoer of upright conduct was a true Christian, and every one of poor conduct was a counterfeit. Now I realize that while this judgment is sometimes correct—for many of bad conduct are indeed counterfeits—yet among those who stumble, there are also genuine sheep who have slipped into the ditch through lack of spiritual vigilance.",
        # 71
        "In testing whether a person is truly born again, do not look merely at whether he has stumbled into sin; look far more at his attitude toward sin! A regenerate person can stumble into sin, but under no circumstances can he love sin. An unregenerate person not only sins, but revels in sin and makes it his home. This is the supreme criterion that divides the sheep from the swine.",
        # 72
        "To refrain from leading a sinner to Christ for repentance, faith, and regeneration, and merely attempt to improve his outward environment, strip away a few bad habits, and hope that he will become a good man and sin no more—this is precisely like dragging a pig out of the mud, scrubbing it clean, and perfuming it. You have changed its outward appearance, but you have not changed its inward swine nature!",
        # 73
        "To modify outward circumstances without transforming the inward nature is of zero eternal value. Today, the sermons preached by many ministers on \"social reform and character elevation\" are nothing other than the method of giving a bath to a pig! Such methods will never produce genuine, permanent spiritual fruit.",
        # 74
        "That a born-again person can still sin is due not only to the fact that he lives in an evil, seductive world filled with traps and temptations at every turn, but also because he harbors within him two radically opposing natures:",
        # 75
        "One is earthly, and the other is heavenly; one is depraved and wicked, and the other is holy and good; one was received at the first birth, and the other was received at the second birth. These two natures correspond to the two men we spoke of earlier: the \"outer man\" and the \"inner man.\" These two natures continually war against each other within the believer's breast.",
        # 76
        "For this very reason, Paul wrote to the church at Ephesus: \"For this reason I bow my knees before the Father, from whom every family in heaven and on earth is named, that according to the riches of His glory He may grant you to be strengthened with power through His Spirit in the inner man...\" (Ephesians 3:14–16).",
        # 77
        "While living in this present world, the children of God are perpetually assaulted by three formidable enemies: One enemy is their own flesh—the outer man; another enemy is the host of demonic spirits ruling the air; and the third enemy is this wicked world that lies under the sway of Satan.",
        # 78
        "Looking at the battle purely from a human standpoint, we would appear to have not the faintest glimmer of hope for victory! Any one of these three enemies would be more than enough to crush us; how much more when all three join forces in a concerted assault against us! The sinful world surrounds us on every side; Satan launches fiery darts from the air; and our fallen flesh rises up from within in treacherous alliance! To borrow an analogy from modern warfare: it is as if an army were completely besieged on land and sea, subjected to relentless aerial bombardment from above, and undermined from within by a traitorous Fifth Column! It seems impossible even to hold the defensive lines, let alone dream of triumph!",
        # 79
        "Thanks be to God, through His living Word we know with unshakeable certainty that although we are hard-pressed on every side, we possess glorious hope of total victory! For our Commander, Jesus Christ, has already vanquished every foe! He is alive forevermore; He stands by us to sustain and fortify our strength; He marches at our head to lead us against these ferocious enemies. Through Him, we are not only conquerors, but more than conquerors! If only we believe in Him, rely upon Him, draw near to Him, and obey His commands, we will surely discover that His grace is all-sufficient for us, and His power is made perfect in our weakness!",
        # 80
        "Then we shall cry out in triumphant joy with the Apostle Paul: \"Therefore I will boast all the more gladly of my weaknesses, so that the power of Christ may rest upon me... For when I am weak, then I am strong!\" (2 Corinthians 12:9–10)."
    ]
    return translations

def build_ch5_file():
    with open('cszy_raw/true_paragraphs_book.json', 'r', encoding='utf-8') as f:
        book = json.load(f)
    
    ch5_paras = book[5]['paragraphs']
    translations = get_ch5_translations()
    
    assert len(ch5_paras) == len(translations), f"Mismatch: {len(ch5_paras)} vs {len(translations)}"
    
    lines = [
        "# 《重生真意》（中英双语对照版）",
        "## 五、得了重生的人还能犯罪吗？ / Chapter 5: Can a Person Who Is Born Again Still Sin?",
        "",
        "---",
        ""
    ]
    
    for i, (zh, en) in enumerate(zip(ch5_paras, translations)):
        lines.append("### 【中文】")
        lines.append(zh)
        lines.append("")
        lines.append("### 【English】")
        lines.append(en)
        lines.append("")
        lines.append("---")
        lines.append("")
        
    content = "\n".join(lines)
    with open('cszy_translation/05_chapter5.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully generated cszy_translation/05_chapter5.md with {len(ch5_paras)} bilingual sections!")

if __name__ == '__main__':
    build_ch5_file()
