In [22]: len(list(Subtitle.objects.filter(subtitles__published=True, start__gt=F("end")).values("id", "subtitles_id", "start", "end")))
Out[22]: 9

In [23]: list(Subtitle.objects.filter(subtitles__published=True, start__gt=F("end")).values("id", "subtitles_id", "start", "end"))
Out[23]: 
[{'id': 1415288,
  'subtitles_id': 'fd9e5ff1-0b00-46c6-9866-c0c6042cc3fa',
  'start': 492200,
  'end': 492160},
 {'id': 4223043,
  'subtitles_id': '10f54631-6976-4e6e-ba1f-171492414b5d',
  'start': 112440,
  'end': 112400},
 {'id': 4223045,
  'subtitles_id': '10f54631-6976-4e6e-ba1f-171492414b5d',
  'start': 114040,
  'end': 114000},
 {'id': 4223047,
  'subtitles_id': '10f54631-6976-4e6e-ba1f-171492414b5d',
  'start': 116000,
  'end': 115960},
 {'id': 4223049,
  'subtitles_id': '10f54631-6976-4e6e-ba1f-171492414b5d',
  'start': 118120,
  'end': 118080},
 {'id': 4223051,
  'subtitles_id': '10f54631-6976-4e6e-ba1f-171492414b5d',
  'start': 120400,
  'end': 120360},
 {'id': 8522499,
  'subtitles_id': 'b3ba0870-cb97-4791-9ce7-35da83a91cde',
  'start': 735568,
  'end': 735567},
 {'id': 8522534,
  'subtitles_id': 'b3ba0870-cb97-4791-9ce7-35da83a91cde',
  'start': 870672,
  'end': 870671},
 {'id': 11866294,
  'subtitles_id': '6b059ce7-a861-410c-ba04-2b688c674a64',
  'start': 522360,
  'end': 522320}]

In [24]: len(list(Subtitle.objects.filter(subtitles__published=True, start=F("end")).values("id", "subtitles_id", "start", "end")))
Out[24]: 27

In [25]: list(Subtitle.objects.filter(subtitles__published=True, start=F("end")).values("id", "subtitles_id", "start", "end"))
Out[25]: 
[{'id': 6511583,
  'subtitles_id': '1658114e-543c-4526-8ac9-57b60b9ea27c',
  'start': 200402,
  'end': 200402},
 {'id': 6512069,
  'subtitles_id': '1658114e-543c-4526-8ac9-57b60b9ea27c',
  'start': 1411670,
  'end': 1411670},
 {'id': 6513351,
  'subtitles_id': 'a4d0462c-5d6e-4fa1-90b2-1bcb3b84b791',
  'start': 310833,
  'end': 310833},
 {'id': 6513360,
  'subtitles_id': 'a4d0462c-5d6e-4fa1-90b2-1bcb3b84b791',
  'start': 327136,
  'end': 327136},
 {'id': 6513560,
  'subtitles_id': 'a4d0462c-5d6e-4fa1-90b2-1bcb3b84b791',
  'start': 744319,
  'end': 744319},
 {'id': 6579128,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 308115,
  'end': 308115},
 {'id': 6579165,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 375248,
  'end': 375248},
 {'id': 6579534,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 1245097,
  'end': 1245097},
 {'id': 6579551,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 1276745,
  'end': 1276745},
 {'id': 6579558,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 1290172,
  'end': 1290172},
 {'id': 6579804,
  'subtitles_id': 'c3cba502-1499-49df-bf9f-7e093937b28d',
  'start': 1879981,
  'end': 1879981},
 {'id': 6585582,
  'subtitles_id': '699ea539-aa1d-4d2d-b88d-f7b1aa76d805',
  'start': 1033226,
  'end': 1033226},
 {'id': 13242354,
  'subtitles_id': '99676288-1a19-40e7-9bf0-852857777414',
  'start': 703040,
  'end': 703040},
 {'id': 8522548,
  'subtitles_id': 'b3ba0870-cb97-4791-9ce7-35da83a91cde',
  'start': 926734,
  'end': 926734},
 {'id': 19943134,
  'subtitles_id': '924cfd72-6a0b-43ea-820f-2c3ea4ca9442',
  'start': 93360,
  'end': 93360},
 {'id': 16152832,
  'subtitles_id': '92ba5c8a-7252-4059-b616-2aec29925a13',
  'start': 0,
  'end': 0},
 {'id': 21805720,
  'subtitles_id': '80be4c90-c310-40d3-a3e4-d909d8c32039',
  'start': 8181640,
  'end': 8181640},
 {'id': 22364903,
  'subtitles_id': 'a0e9ae23-05ad-4f1e-823a-565d4d66101c',
  'start': 359999999,
  'end': 359999999},
 {'id': 23610020,
  'subtitles_id': '446069f5-6837-4477-a0f4-a45706cdd400',
  'start': 0,
  'end': 0},
 {'id': 23613326,
  'subtitles_id': '53c8ac5f-d183-43f1-a5f2-ba19943a62be',
  'start': 0,
  'end': 0},
 {'id': 24344482,
  'subtitles_id': '4219078f-2874-4d0d-8dc2-cffc6fb2c45c',
  'start': 0,
  'end': 0},
 {'id': 24345403,
  'subtitles_id': 'b7f0ca07-6eeb-42ce-8038-906d2d2d5f31',
  'start': 0,
  'end': 0},
 {'id': 24346522,
  'subtitles_id': '37ae3789-225d-4bec-85d8-175e0200aa56',
  'start': 0,
  'end': 0},
 {'id': 24347521,
  'subtitles_id': '0cb8ab68-5030-4706-ba5c-dca5b620c639',
  'start': 0,
  'end': 0},
 {'id': 24348589,
  'subtitles_id': '9d02f4b8-677f-4001-b208-2f384ac279e5',
  'start': 0,
  'end': 0},
 {'id': 24349639,
  'subtitles_id': '6c80600b-48d5-4c86-937b-afaf9b1ef77e',
  'start': 0,
  'end': 0},
 {'id': 24350715,
  'subtitles_id': '90520091-c852-4379-8138-d494521f4f33',
  'start': 0,
  'end': 0}]