from argparse import ArgumentParser
from ffmpeg import FFmpeg

def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("rate", type=int)
    args = parser.parse_args()
            
    ffmpeg = (
        FFmpeg()
            .option("y")
            .input(args.input)
            .output(args.output,
                    ar=args.rate)
    )

    ffmpeg.execute()

if __name__ == "__main__":
    main()
