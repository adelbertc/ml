let
  nixpkgs = fetchGit {
    url = "https://github.com/NixOS/nixpkgs.git";
    rev = "8130f3c1c2bb0e533b5e150c39911d6e61dcecc2";
  };

  pkgs = import nixpkgs { };
in
  pkgs.mkShell {
    name = "statistical-learning";
    buildInputs = with pkgs; [
      python37
      poetry
      mypy
      python37Packages.black
      python37Packages.flake8
    ];
  }
