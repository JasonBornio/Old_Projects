using Terraria;
using Terraria.ModLoader;
using System;

namespace SONICMOD.Buffs
{   public abstract class BaseTransformation : ModBuff
    {
        public float DamageMulti;
        public float SpeedMulti;
        public float ChaosDamageMulti;
        public int RingConsumption;
        public float JumpHeightMulti;
        public int AromourPenetrtionBonus;
        public float DefenseMutli;
        public float defenseBonus;
        public float RingUsageMulti;


        public override void Update(Player player, ref int buffIndex)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            defenseBonus = (float)Math.Log(DefenseMutli);
            player.endurance += defenseBonus;
            modPlayer.ChaosDamage *= (ChaosDamageMulti / DamageMulti);
            player.allDamageMult *= DamageMulti;
            player.jumpBoost = true;
            player.runAcceleration += (SpeedMulti - 1);
            player.jumpSpeedBoost += JumpHeightMulti;
            player.moveSpeed *= SpeedMulti;
            player.maxRunSpeed *= SpeedMulti;
            player.accRunSpeed *= SpeedMulti;
            modPlayer.ChaosRunSpeed *= SpeedMulti;
            player.armorPenetration += AromourPenetrtionBonus;
        }
    }
}
