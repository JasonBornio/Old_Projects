using System;
using Microsoft.Xna.Framework;
using Terraria;
using Terraria.Graphics.Effects;
using Terraria.Graphics.Shaders;
using Terraria.ID;
using Terraria.ModLoader;

namespace SONICMOD.Items.Weapons
{
    public class BoxingGloves : ChaosItem
    {
        public override void SetStaticDefaults()
        {
            DisplayName.SetDefault("Boxing Glove (Left)");
            Tooltip.SetDefault("Yo");
        }
        public override void SetDefaults()
        {
            item.damage = 10;
            item.melee = true;
            item.width = 50;
            item.height = 50;
            item.useTime = 5;
            item.useStyle = ItemUseStyleID.SwingThrow;
            item.useAnimation = 16;
            item.knockBack = 1;
            item.value = 10;
            item.rare = ItemRarityID.Purple;
            item.UseSound = SoundID.Item1;
            item.autoReuse = true;
            item.maxStack = 1;
            item.consumable = false;


        }

    }
}
