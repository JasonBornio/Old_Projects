using Terraria;
using System;
using Terraria.ModLoader;


namespace SONICMOD.Buffs.TransformationBuffs
{

    public class Hyper : BaseTransformation
    {
        public override void SetDefaults()
        {
            DisplayName.SetDefault("Hyper");
            Description.SetDefault("You are powered all 7 Super Emeralds");
            Main.buffNoTimeDisplay[Type] = true;
            Main.debuff[Type] = false;
            DamageMulti = 2.5f;
            SpeedMulti = 1.75f;
            ChaosDamageMulti = 4.0f;
            RingConsumption = 7;
            JumpHeightMulti = 2.5f;
            AromourPenetrtionBonus = 7;
            DefenseMutli = 1.5f;
            RingUsageMulti = 1.35f;
        }

        public override void Update(Player player, ref int buffIndex)
        {
            base.Update(player, ref buffIndex);
        }
    }
   
}
