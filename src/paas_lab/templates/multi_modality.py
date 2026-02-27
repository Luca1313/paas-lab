from datapizza.type import Media, TextBlock, MediaBlock

from paas_lab.utils.openai_client import client


def main():
    media = Media(
        extension="jpg",
        media_type="image",
        source_type="path",
        source="old-dataset/dataset-2025/png/pizzaverse.png",
    )

    response = client.invoke(
        [
            TextBlock(content="Please describe the content of this image"),
            MediaBlock(media=media),
        ]
    )
    print(response.text)


if __name__ == "__main__":
    main()
