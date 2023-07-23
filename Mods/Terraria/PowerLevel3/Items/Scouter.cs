using System;
using System.Linq;
using System.Runtime.CompilerServices;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Terraria.Localization;
using System.Collections.Generic;
using Microsoft.Xna.Framework;


namespace PowerLevel3.Items
{
    class Scouter : ModItem
    {
        private readonly Mod dbzMod = ModLoader.GetMod("DBZMOD");
        private readonly Mod LootMod = ModLoader.GetMod("Loot");
        public override bool Autoload(ref string name)
        {
            return ModLoader.GetMod("DBZMOD") != null &&
            ModLoader.GetMod("Loot") != null;
        }
        public override void SetStaticDefaults()
        {
            DisplayName.SetDefault("Scouter");
        }

        public override void SetDefaults()
        {

            item.width = 20;
            item.height = 20;
            item.value = Item.sellPrice(silver: 30);
        }


        public override void ModifyTooltips(List<TooltipLine> tooltips)
        {
            if (!PowerLevel3.instance.DBTLoaded || 
                !PowerLevel3.instance.LootLoaded) return;

            Player player = Main.player[item.owner];
            DBZMOD.MyPlayer dbtPlayer = player.GetModPlayer<DBZMOD.MyPlayer>();
            Loot.ModifierPlayer mplayer = player.GetModPlayer<Loot.ModifierPlayer>();
            Loot.Modifiers.EquipModifiers.Defensive.ManaShieldEffect manaShield = mplayer.GetEffect<Loot.Modifiers.EquipModifiers.Defensive.ManaShieldEffect>();



            tooltips.Add(new TooltipLine(mod, "info", $"multdefense: {(int)Math.Ceiling((0.5) * player.statDefense)}BIL"));
            tooltips.Add(new TooltipLine(mod, "info", $"defense: {player.statDefense}"));
            double PL;
            double endurance = Math.Pow(1000, (player.endurance + manaShield.ManaShield));
            PL = (double)(((player.statDefense + (dbtPlayer.kiChargeRate - 1) * 3 + dbtPlayer.kiMax2 / 15 + dbtPlayer.kiSpeedAddition + dbtPlayer.kiKbAddition + player.statLife / 25f + player.statMana / 12.5f +

            ((player.accRunSpeed + player.maxRunSpeed) / 2f * player.moveSpeed * 6) / 6f + (player.wingTimeMax / 120f) + (player.jumpSpeedBoost) + dbtPlayer.flightSpeedAdd * (dbtPlayer.flightUsageAdd + 1))) *

            ((((1 + ((dbtPlayer.kiCrit / 100 + 0.95f) - 1) * 30f) + (1 + ((player.magicCrit / 100 + 0.96f) - 1) * 8f) + (1 + ((player.rangedCrit / 100 + 0.96f) - 1) * 8f) + (1 + ((player.meleeCrit / 100 + 0.96f) - 1) * 8f))/4 + ((player.maxMinions * player.maxTurrets) / 5f)) * 0.25f) *

            (((1 + (player.meleeDamage - 1) * 15f) + (1 + (player.rangedDamage - 1) * 15f) + (1 + (player.magicDamage - 1) * 15f) + (1 + (player.minionDamage - 1) * 15f) + (1 + (dbtPlayer.kiDamage - 1) * 50f)) / 5 + (player.armorPenetration) / 5f) *

            ((2f + dbtPlayer.masteryLevel1 * 1.5f + dbtPlayer.masteryLevel2 * 1.5f + dbtPlayer.masteryLevel3 * 1.5f) * 0.5f) *

            (player.magicDamageMult * player.meleeDamageMult * player.allDamageMult * player.rangedDamageMult * player.minionDamageMult * (dbtPlayer.kiRegen / 5 + 1) * (dbtPlayer.kiMaxMult * 3)));
            //
            tooltips.Add(new TooltipLine(mod, "info", $"sheild Power: {manaShield.ManaShield}"));
            //
            if (PL > 1000000000)
            {
                PL /= 1000000000;
                if (endurance * PL > 1000f && endurance * PL < 1000000f)
                {
                    PL = (double)((PL * endurance) / 1000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}TRIL"));
                }
                else if (endurance * PL > 1000000f && endurance * PL < 1000000000f)
                {
                    PL = (double)((PL * endurance) / 1000000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}QUAD"));
                }
                else
                {
                    PL = (double)(PL * endurance);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}BIL"));
                }
            }
            else if (PL > 1000000)
            {
                PL /= 1000000;
                if (endurance * PL > 1000f && endurance * PL < 1000000f)
                {
                    PL = (double)((PL * endurance) / 1000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}BIL"));
                }
                else if (endurance * PL > 1000000f && endurance * PL < 1000000000f)
                {
                    PL = (double)((PL * endurance) / 1000000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}TRIL"));
                }
                else
                {
                    PL = (double)(PL * endurance);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}MIL"));
                }

            }
            else if (PL > 1000)
            {
                PL /= 1000;
                if (endurance * PL > 1000f && endurance * PL < 1000000f)
                {
                    PL = (double)((PL * endurance) / 1000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}MIL"));
                }
                else if (endurance * PL > 1000000f && endurance * PL < 1000000000f)
                {
                    PL = (double)((PL * endurance) / 1000000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}BIL"));
                }
                else
                {
                    PL = (double)(PL * endurance);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}K"));
                }
            }
            else if (PL < 0)
            {
                tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: Unreadable"));
            }
            else
            {
                if (endurance * PL > 1000f && endurance * PL < 1000000f)
                {
                    PL = (double)((PL * endurance) / 1000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}K"));
                }
                else if (endurance * PL > 1000000f && endurance * PL < 1000000000f)
                {
                    PL = (double)((PL * endurance) / 1000000);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}MIL"));
                }
                else
                {
                    PL = (double)(PL * endurance);
                    tooltips.Add(new TooltipLine(mod, "info", $"Battle Power: {(double)Math.Round(PL, 3)}"));
                }
            }



        }

    }
}