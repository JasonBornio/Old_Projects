using System.Collections.Generic;
using System.Linq;
using Terraria;
using Terraria.ModLoader;
using Terraria.Utilities;
using Microsoft.Xna.Framework;
using System;

namespace SONICMOD
{
    public abstract class ChaosItem : ModItem
    {
        public static bool chaos = true;
        public override void SetDefaults()
        {
            item.melee = false;
            item.ranged = false;
            item.magic = false;
            item.thrown = false;
            item.summon = false;

        }


        public override void ModifyTooltips(List<TooltipLine> tooltips)
        {
            var tt = tooltips.FirstOrDefault(x => x.Name == "Damage" && x.mod == "Terraria");
            if (tt != null)
            {
                string[] split = tt.text.Split(' ');
                tt.text = split.First() + " chaos " + split.Last();
            }
        }
        public override void GetWeaponDamage(Player player, ref int damage)
        {
            HPlayer modPlayer = player.GetModPlayer<HPlayer>();
            int originalDamage = damage;
            damage = (int)(damage * (modPlayer.ChaosDamage));// + (player.allDamageMult - 1)));
            float globalDmg = 1f;
            globalDmg = player.meleeDamage - 1;
            if (player.magicDamage - 1 < globalDmg)
                globalDmg = player.magicDamage - 1;
            if (player.rangedDamage - 1 < globalDmg)
                globalDmg = player.rangedDamage - 1;
            if (player.thrownDamage - 1 < globalDmg)
                globalDmg = player.thrownDamage - 1;
            if (player.minionDamage - 1 < globalDmg)
                globalDmg = player.minionDamage - 1;
            if (globalDmg > 1)
                damage = damage + (int)(originalDamage * globalDmg);

        }
        public override void GetWeaponCrit(Player player, ref int crit)
        {
            HPlayer modPlayer = player.GetModPlayer<HPlayer>();
            crit = crit + modPlayer.ChaosCrit;
        }
    }
}
