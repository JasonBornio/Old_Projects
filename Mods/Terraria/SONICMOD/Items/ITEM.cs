using System;
using System.Linq;
using System.Runtime.CompilerServices;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Terraria.Localization;
using System.Collections.Generic;
using Microsoft.Xna.Framework;

namespace SONICMOD.Items
{
    public class ITEM : ModItem
    {

        public override void SetStaticDefaults()
        {
            DisplayName.SetDefault("ITEM");
        }

        public override void SetDefaults()
        {

            item.width = 20;
            item.height = 20;
            item.value = Item.sellPrice(silver: 30);
        }


        public override void ModifyTooltips(List<TooltipLine> tooltips)
        {
            Player player = Main.player[item.owner];
            HPlayer modPlayer = HPlayer.ModPlayer(player);

            tooltips.Add(new TooltipLine(mod, "info", $"posX: {modPlayer.posX}"));
            tooltips.Add(new TooltipLine(mod, "info", $"posY: {modPlayer.posY}"));


        }

    }

}
