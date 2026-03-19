import access_control as ac
import media_engine as me

# --- INITIAL SETUP ---
CONTROL_NUM = 2 
FAVORITE_ARTIST = "TAYLOR SWIFT"
ARTIST_LEN = len(FAVORITE_ARTIST)

print(f"--- CONFIG: CONTROL_NUM={CONTROL_NUM}, ARTIST={FAVORITE_ARTIST} ---")

# --- EXERCISE 1 ---
print("\n[EXERCISE 1]")
@ac.audit_log
def run_auth():
    lvl = (CONTROL_NUM * 3) + ARTIST_LEN
    decision = ac.validate_access(lvl, CONTROL_NUM)
    print(f"Computed Access Level: {lvl}")
    print(f"Threshold Applied: {CONTROL_NUM * 5}")
    print(f"Final Authorization Decision: {decision}")

run_auth()

# --- EXERCISE 2 ---
print("\n[EXERCISE 2]")
def signal_shutdown(power, count=0):
    if power <= 0:
        print(f"Base case reached: power == {power}")
        return count + 1
    print(f"Current signal strength: {power}")
    return signal_shutdown(power - 1, count + 1)

initial_pwr = CONTROL_NUM + ARTIST_LEN
calls = signal_shutdown(initial_pwr)
print(f"Initial Signal Strength: {initial_pwr}")
print(f"Total Recursive Calls: {calls}")

# --- EXERCISE 3 ---
print("\n[EXERCISE 3]")
limit = CONTROL_NUM + ARTIST_LEN
# Tatawagin na ang function mula sa media_engine module
counts = me.play_count_stream(limit)

print(f"Computed Stream Limit: {limit}")
print(f"Generated Play Counts: {counts}")
print(f"Total Plays: {sum(counts)}")
print(f"Number of Records Processed: {len(counts)}")