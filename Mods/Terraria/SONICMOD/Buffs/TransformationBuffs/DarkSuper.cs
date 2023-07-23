using Terraria;
using System;
using Terraria.ModLoader;


namespace SONICMOD.Buffs.TransformationBuffs
{
    public class DarkSuper : BaseTransformation
    {
        public override void SetDefaults()
        {
            DisplayName.SetDefault("Dark Super");
            Description.SetDefault("You feed off of the negative chaotic energy");
            Main.buffNoTimeDisplay[Type] = true;
            Main.debuff[Type] = false;
            DamageMulti = 1.75f;
            SpeedMulti = 1.3875f;
            ChaosDamageMulti = 2.5f;
            RingConsumption = 4;
            JumpHeightMulti = 1.75f;
            AromourPenetrtionBonus = 5;
            DefenseMutli = 1.2f;
            RingUsageMulti = 1.0f;

        }

        public override void Update(Player player, ref int buffIndex)
        {
            base.Update(player, ref buffIndex);
        }
    }

}
