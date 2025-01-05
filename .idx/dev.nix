# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  channel = "stable-24.05";
  
  packages = with pkgs; [
    (python312.withPackages (ps: with ps; [
      fastapi
      uvicorn
      pydantic
    ]))
  ];

  env = {
    PYTHONPATH = "./";
  };

  idx.extensions = [
    "ms-python.python"
  ];
}