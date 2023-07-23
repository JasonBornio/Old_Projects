
using Microsoft.Xna.Framework;
using System.Collections.Generic;
using Terraria;
using Terraria.ModLoader;
using Terraria.UI;
using Microsoft.Xna.Framework.Graphics;
using Terraria.Graphics.Shaders;
using Terraria.Graphics.Effects;
using System.IO;

namespace SONICMOD
{
	public class SONICMOD : Mod
	{
		public static SONICMOD instance;
		public SONICMOD()
		{
			Properties = new ModProperties
			{
				Autoload = true,
				AutoloadGores = true,
				AutoloadSounds = true
			};
		}


		public override void Unload()
		{
			instance = null;
		}

		public override void Load()
		{
			instance = this;
			HPlayer.Transform = RegisterHotKey("Turn Super", "V");
			HPlayer.PowerDown = RegisterHotKey("Power Down", "X");
		}

		public static uint GetTicks()
		{
			return Main.GameUpdateCount;
		}

		public static bool IsTickRateElapsed(int i)
		{
			return GetTicks() > 0 && GetTicks() % i == 0;
		}

	}
}