# To learn more about how to use Nix to configure your environment
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
      # Dependencias para base de datos
      aiosqlite
      alembic
      asyncpg
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