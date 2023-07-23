using Terraria;
using Terraria.ModLoader;

namespace SONICMOD.Buffs.BuffsANDDebuffs
{
    public class HomingAttackDebuff : ModBuff
    {

        public override void SetDefaults()
        {
            Main.debuff[Type] = true;
        }
        
        public override void Update(NPC npc, ref int buffIndex)
        {
            Player player = Main.player[0];
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            npc.life -= (int)(50 * modPlayer.ChaosDamage);
            npc.justHit = true;
            npc.velocity.X = -5 * player.direction;
            
        }
    }
}

