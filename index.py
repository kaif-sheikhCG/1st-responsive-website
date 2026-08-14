import random
import time

def battle_simulation():
    print("⚔️ WELCOME TO THE ARENA! ⚔️\n")
    
    # Initialize character health
    player_health = 100
    monster_health = 100
    
    # List of possible random battle events
    events = [
        "A sudden dust storm makes it hard to see!",
        "The crowd cheers loudly, energizing both fighters!",
        "The ground shakes violently!",
        "A passing bird distracts the arena!"
    ]

    # Main game loop
    while player_health > 0 and monster_health > 0:
        print(f"❤️ Player HP: {player_health} | 👹 Monster HP: {monster_health}")
        print("-" * 40)
        
        # 1. Player Turn
        input("Press Enter to swing your sword...")
        
        # Dynamic damage range using random.randint
        player_damage = random.randint(10, 25) 
        
        # 10% chance for a critical hit (random float between 0.0 and 1.0)
        if random.random() < 0.10: 
            player_damage *= 2
            print(f"💥 CRITICAL HIT! You dealt {player_damage} damage!")
        else:
            print(f"⚔️ You strike the monster for {player_damage} damage.")
            
        monster_health -= player_damage
        time.sleep(1) # Dramatic pause
        
        # Check if monster died
        if monster_health <= 0:
            break
            
        # 2. Random Arena Event (20% chance)
        if random.random() < 0.20:
            random_event = random.choice(events)
            print(f"\n📢 EVENT: {random_event}\n")
            time.sleep(1)

        # 3. Monster Turn
        print("👹 The monster prepares to counter-attack...")
        time.sleep(1)
        
        # Monster damage range
        monster_damage = random.randint(12, 22)
        
        # 15% chance the monster misses completely
        if random.random() < 0.15:
            print("💨 The monster swung wildly and MISSED!")
        else:
            print(f"💥 The monster bashes you for {monster_damage} damage.")
            player_health -= monster_damage
            
        print("\n" + "="*40 + "\n")
        time.sleep(1)

    # Game Over logic
    print("🏆 BATTLE OVER 🏆")
    if player_health > 0:
        print("🎉 Victory! You defeated the monster and survived yayyyy!")
    else:
        print("💀 Defeat! The monster overpowered you. Game Over.")

# Run the game
battle_simulation()
