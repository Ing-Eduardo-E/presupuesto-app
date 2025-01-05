# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  channel = "stable-24.05";

  packages = with pkgs; [
    (python312.withPackages (ps: with ps; [
      fastapi
      uvicorn
      sqlalchemy
      pydantic
      pydantic-settings
      python-dotenv
    ]))
  ];

  env = {
    PYTHONPATH = "./backend";
  };

  idx.extensions = [
    "ms-python.python"
    "ms-python.vscode-pylance"
  ];
}