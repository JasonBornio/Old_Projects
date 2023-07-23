using Terraria;
using Terraria.ModLoader;
using System;

namespace SONICMOD.Buffs.BuffsANDDebuffs
{
    public class HomingAttackBuff : ModBuff
    {

        public override void SetDefaults()
        {
            DisplayName.SetDefault("Homing");
            Main.buffNoTimeDisplay[Type] = true;
            Main.debuff[Type] = false;
        }

        public override void Update(Player player, ref int buffIndex)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            player.statDefense += (int)(player.statDefense * 0.1f);
        }
    }
}

