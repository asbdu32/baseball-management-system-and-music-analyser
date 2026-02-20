import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--players',
    nargs='+',
    required=False,  # ✅ make it optional
    default=['Shohei Ohtani', 'Aaron Judge'],  # ✅ default values
    help='List of player names (optional)'
)

parser.add_argument('--years', nargs=2, type=int, help='Start and end years')
parser.add_argument('--fetch', action='store_true', help='Fetch new data')
parser.add_argument('--outdir', type=str, help='Output directory')
args = parser.parse_args()
import argparse

parser = argparse.ArgumentParser()

# Make players optional with a default list
parser.add_argument(
    '--players',
    nargs='+',
    required=False,
    default=['Shohei Ohtani', 'Aaron Judge'],  # 👈 default players for testing
    help='List of player names'
)

# Other optional arguments can also have defaults
parser.add_argument('--years', nargs=2, type=int, default=[2022, 2024], help='Start and end years')
parser.add_argument('--fetch', action='store_true', help='Fetch new data')
parser.add_argument('--outdir', type=str, default='results', help='Output directory')

args = parser.parse_args()

print(f"Comparing players: {args.players}")
print(f"Years: {args.years}")
print(f"Output directory: {args.outdir}")
