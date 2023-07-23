using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using System;
using System.Collections.Generic;
using System.IO;
using Terraria;
using Terraria.ID;
using Terraria.Localization;
using Terraria.ModLoader;
using Terraria.UI;

namespace PowerLevel3
{
	public class PowerLevel3 : Mod
	{
		public bool LootLoaded;
		public bool DBTLoaded;
		public static PowerLevel3 instance;

		public PowerLevel3()
		{
			Properties = new ModProperties
			{
				Autoload = true,
				AutoloadGores = true,
				AutoloadSounds = true
			};
		}

		public override void Load()
		{
			instance = this;
			LootLoaded = ModLoader.GetMod("Loot") != null;
			DBTLoaded = ModLoader.GetMod("DBZMOD") != null;
		}

	}
			
}