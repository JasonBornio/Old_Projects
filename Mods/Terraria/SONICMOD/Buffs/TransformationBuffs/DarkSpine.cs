using Terraria;
using System;
using Terraria.ModLoader;

namespace SONICMOD.Buffs.TransformationBuffs
{
    public class DarkSpine: BaseTransformation
    {
        public override void SetDefaults()
        {
            DisplayName.SetDefault("Dark Spine");
            Description.SetDefault("You are powered all 7 Secret Rings");
            Main.buffNoTimeDisplay[Type] = true;
            Main.debuff[Type] = false;
            DamageMulti = 1.4f;
            SpeedMulti = 1.2f;
            ChaosDamageMulti = 1.8f;
            RingConsumption = 2;
            JumpHeightMulti = 1.4f;
            AromourPenetrtionBonus = 3;
            DefenseMutli = 1.15f;
            RingUsageMulti = 1.75f;

        }

        public override void Update(Player player, ref int buffIndex)
        {
            base.Update(player, ref buffIndex);
        }
    }
}
