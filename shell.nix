let
  pkgs_main = import (fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/a0374025a863.tar.gz"; # 26.05 - https://github.com/NixOS/nixpkgs/commit/a0374025a863d007d98e3297f6aa46cc3141c2f0
    sha256 = "14c0hqipkcm2iqi5ybjpx4xcvwxjp3sx3rfgb69dv83h0gm1crgn";
  }) { };
in
pkgs_main.mkShell {
  buildInputs = [
    pkgs_main.opentofu
    pkgs_main.elmPackages.elm
    pkgs_main.elmPackages.elm-format
  ];

  shellHook = ''
    source .venv/bin/activate
  '';
}
