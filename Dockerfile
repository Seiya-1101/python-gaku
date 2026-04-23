# uv の公式イメージはパッチバージョンを固定できないので使用しません
# また、Alpine ではなく Debian ベースのイメージを使用します
# Python で Alpine イメージを使うと次のデメリットがあるため:
# - ビルドがとても遅くなります
# - イメージが大きくなります
# - 時間を浪費することになります
# - 場合によってはよくわからないランタイムのバグが発生します
# 詳細は次の記事を参照お願いします:
# - Using Alpine can make Python Docker builds 50× slower
#   https://pythonspeed.com/articles/alpine-docker-python/
FROM python:3.13.5-slim-bookworm
# .devcontainer/devcontainer.json の workspaceFolder で指定したディレクトリーと
# 同じにします
# 上記のディレクトリーに開発用の Python 仮想環境を作成する必要があるため
WORKDIR /workspace
# uv 公式が推奨するインストール方法です
# メリットはおそらく次の通りです:
# - Docker によってキャッシュされるので、Docker イメージの再ビルドが速くなります
# - uv が pip の依存関係にならなくなります
# Using uv in Docker | uv
# https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.7.15 /uv /uvx /bin/
COPY pyproject.toml uv.lock /workspace/
# インストール時にダウンロードする依存関係 Python パッケージを
# Docker Volume にキャッシュします
# これにより、Docker イメージの再ビルドが速くなります
# uv 公式が推奨する Python プロジェクト依存関係 Python パッケージインストール方法です:
# - Using uv in Docker | uv
#.  https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync