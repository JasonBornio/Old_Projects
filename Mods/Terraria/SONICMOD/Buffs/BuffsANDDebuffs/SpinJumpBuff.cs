using Terraria;
using Terraria.ModLoader;

namespace SONICMOD.Buffs.BuffsANDDebuffs
{
    public class SpinJumpBuff : ModBuff
    {
        public override void SetDefaults()
        {
            DisplayName.SetDefault("Defensive Buff");
            Description.SetDefault("Grants +4 defense.");
            Main.buffNoTimeDisplay[Type] = false;
            Main.debuff[Type] = false;
        }

        public override void Update(Player player, ref int buffIndex)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            player.statDefense += 25;
            player.jumpSpeedBoost += 0.5f;
            player.moveSpeed += 1;
            player.jumpBoost = true;
            player.thorns += modPlayer.SpinDamage;
            player.maxFallSpeed += 1;
       
        }
    }
}

