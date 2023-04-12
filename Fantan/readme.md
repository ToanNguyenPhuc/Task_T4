## :video_game: Action

  Action_size: 53
  [0:52]: Bài muốn đánh
  [52]: bỏ lượt


## :bust_in_silhouette: Player_state
  Giá trị bài: k % 13
  Giá trị bài bắt đầu từ 0 -> 51
  0 là 1, 1 là 2 ...
  Loại bài: k // 13
  0,1,2,3: Cơ, rô, chuồn, bích
  [0:52]: Player card
  [52:104] : Những lá có thể đánh
  [105:108]: Độ dài lá bài còn lại của 3 người chơi
  [108]: Game đã kết thúc hay chưa
  [109:112]: Chip của 3 người chơi


## :globe_with_meridians: env

  [0:8]: 8 lá có thể đánh trên bàn
  [8:21]: Bài người chơi 1
  [22:35]: Bài người chơi 2
  [36:49]: Bài người chơi 3
  [50:63]: Bài người chơi 4
  [21,35,49,63]: chip của 4 người chơi
  env[64]: Id người chơi
  env[65]: Hũ chip chung
  env[66]: Game đã kết thúc hay chưa

