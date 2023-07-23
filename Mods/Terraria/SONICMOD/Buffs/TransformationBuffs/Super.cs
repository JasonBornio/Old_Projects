using Terraria;
using System;
using Terraria.ModLoader;

namespace SONICMOD.Buffs.TransformationBuffs
{
    public class Super : BaseTransformation
    {
        public override void SetDefaults()
        {
            DisplayName.SetDefault("Super");
            Description.SetDefault("You are powered all 7 Chaos Emeralds");
            Main.buffNoTimeDisplay[Type] = true;
            Main.debuff[Type] = false;
            DamageMulti = 1.25f;
            SpeedMulti = 1.125f;
            ChaosDamageMulti = 1.5f;
            RingConsumption = 1;
            JumpHeightMulti = 1.25f;
            AromourPenetrtionBonus = 2;
            DefenseMutli = 1.1f;
            RingUsageMulti = 1.2f;

        }

        public override void Update(Player player, ref int buffIndex)
        {
            base.Update(player, ref buffIndex);
        }
    }
}
