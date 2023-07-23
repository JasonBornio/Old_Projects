using System;
using System.Linq;
using System.Runtime.CompilerServices;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Terraria.Localization;
using System.Collections.Generic;
using Microsoft.Xna.Framework;

namespace PowerLevel3.Buffs
{
	class MasteredSsj : ModItem
	{
        private readonly Mod dbzMod = ModLoader.GetMod("DBZMOD");

        public override bool Autoload(ref string name)
        {
            return ModLoader.GetMod("DBZMOD") != null;
        }
        public override void SetStaticDefaults()
        {
            DisplayName.SetDefault("Mastered Charm");

            Tooltip.SetDefault(
            @"Your Trainig has paid off, 
and now you can handle the Super Saiyajin
form for hours on end with minimal energy 
drain
-This only applies if you have mastered 
all Ssj Forms-

While Transformed:

15% increased endurance
50% increased non-ki damage
75% decreased ki drain;
200% max ki;
Massively increased ki regen 
increased ki charge rate");
        }

        public override void ModifyTooltips(List<TooltipLine> list)
        {
            foreach (TooltipLine tooltipLine in list)
            {
                if (tooltipLine.mod == "Terraria" && tooltipLine.Name == "ItemName")
                {
                    tooltipLine.overrideColor = new Color?(new Color(255, 216, 0));
                }
            }
        }
        public override void SetDefaults()
        {
            item.width = 20;
            item.height = 20;
            item.accessory = true;
            item.value = 1000000;
            item.rare = 11;
        }

        public override void UpdateAccessory(Player player, bool hideVisual)
		{
            
            if (!PowerLevel3.instance.DBTLoaded) return;

            DBZMOD.MyPlayer dbtPlayer = player.GetModPlayer<DBZMOD.MyPlayer>();

            if (dbtPlayer.isTransformed == true && dbtPlayer.masteryLevel1 == 1 && dbtPlayer.masteryLevel2 == 1 && dbtPlayer.masteryLevel3 == 1)
            {
                //DBZMOD.Buffs.SSJBuffs.kiDrainRateWithMastery = 0f;
                player.endurance += 0.15f;
                dbtPlayer.kiDrainMulti -= 0.75f;
                dbtPlayer.kiRegen += 15;
                player.allDamageMult += 0.5f;
                dbtPlayer.kiMaxMult += 2;
                dbtPlayer.kiChargeRate += 5;
            }
		}

        private readonly string[] _items =
        {
            "CrystalliteAlleviate",
            "BuldariumSigmite",
            "EarthenArcanium",
            "KaioCrystal",
            "MajinNucleus",
            "SpiritCharm",
        };

        public override void AddRecipes()
        {
            if (!PowerLevel3.instance.DBTLoaded) return;

            ModRecipe recipe = new ModRecipe(mod);

            foreach (string i in _items)
            {
                recipe.AddIngredient(dbzMod.ItemType(i));
            }

            recipe.AddIngredient(dbzMod.ItemType("PureKiCrystal"), 250);

            recipe.AddTile(dbzMod, "KaiTable");

            recipe.SetResult(this);
            recipe.AddRecipe();
        }
    }			
}

