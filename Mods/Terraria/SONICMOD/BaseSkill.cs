using System;
using Terraria;
using Terraria.ModLoader;
using Microsoft.Xna.Framework;
using Terraria.GameInput;
using Terraria.ID;
using System.Collections.Generic;



namespace SONICMOD
{
    public class BaseSkill
    {
        public static void BallShield(Player player)
        {

        }
        //----------------------------------------------------------       
        public static void ChaosBlast(Player player)
        {

        }
        //----------------------------------------------------------      
        public static void ChaosControl(Player player)
        {

        }
        //----------------------------------------------------------
        public static void ChaosExplosion(Player player)
        {

        }
        //----------------------------------------------------------
        public static void ChaosSphere(Player player)
        {

        }
        public static void Dash(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);

            bool canTP = true;
            

            Vector2 mousePosition = Main.MouseWorld;
            mousePosition.X -= 8;
            mousePosition.Y -= 40;
            Vector2 newVect = (mousePosition - player.position);
            Vector2 direction = Vector2.Normalize(newVect);
            

            if (modPlayer.downTapped && canTP)
            {

            }

            if (modPlayer.dashing) {
                player.velocity = direction * 25;
            }
        
        }
        //----------------------------------------------------------      
        public static void Flight(Player player)
        {

        }
        //----------------------------------------------------------
        public static void HomingAttack(Player player, float distance, NPC closestTarget)
        {
            player.AddBuff(ModContent.BuffType<Buffs.BuffsANDDebuffs.HomingAttackBuff>(), 1);
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            player.fullRotationOrigin = new Vector2(11, 22);
            player.fullRotation = player.fullRotation + 1f * player.direction;

            // kind of redundant, get the offset velocity
            Vector2 offsetVector = closestTarget.Center - player.Center;
            Vector2 normalizedVelocity = (offsetVector * (50 / 20) + player.velocity);
            normalizedVelocity.Normalize();
            Vector2 trueVelocity = normalizedVelocity * 50;
            player.velocity = trueVelocity;
        }//
         //----------------------------------------------------------
        public static void HomingDash(Player player)
        {
            player.AddBuff(ModContent.BuffType<Buffs.BuffsANDDebuffs.HomingAttackBuff>(), 1);
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            player.fullRotationOrigin = new Vector2(11, 22);
            player.fullRotation = player.fullRotation + 1f * player.direction;
            player.velocity.X = 7.5f * player.direction * modPlayer.ChaosRunSpeed;
            player.velocity.Y = 0.1f;
            modPlayer.homingDash = false;
            modPlayer.spinJumping = true;
        }//
        //----------------------------------------------------------
        public static void LightSpeedAttack(Player player)
        {

        }
        //----------------------------------------------------------
        public static void Teleport(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);

            bool canTP = true;

            Vector2 mousePosition = Main.MouseWorld;
            mousePosition.X -= 8;
            mousePosition.Y -= 40;
            Vector2 truePosition = new Vector2();
            Vector2 newVect = (mousePosition - player.position);
            Vector2 postion = Vector2.Normalize(newVect);

            truePosition = (player.position + (postion * 300));

            List<Tile> L = new List<Tile>();

            //Checking all tiles around cursor (on 2x3)
            for (int k = 0; k < 2; k++)
            {
                for (int i = 0; i < 3; i++)
                {
                    L.Add(Main.tile[(int)((truePosition.X + k * 16) / 16f), (int)((truePosition.Y - i * 16) / 16f)]);
                }
            }

            //Checking if any of the tiles around the cursor are active or solid
            //If any is solid or active, then set a bool to false
            L.ForEach(delegate (Tile u)
            {
                if (u.active() == true)
                {
                    if (Main.tileSolid[u.type] == true)
                    {
                        canTP = false;
                    }
                }
            });

            if (modPlayer.downTapped && canTP)
            {
                player.Teleport(truePosition, 1);
                player.velocity = Vector2.Zero;
            }
        }
        //----------------------------------------------------------
        public static void SpinDash(Player player)
        {

        }
        //----------------------------------------------------------
        public static void SpinJump(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            player.fullRotationOrigin = new Vector2(11, 22);

            player.AddBuff(ModContent.BuffType<Buffs.BuffsANDDebuffs.SpinJumpBuff>(), 1);
            player.fullRotation = player.fullRotation + 0.75f * player.direction;

        }//
        //----------------------------------------------------------
    }
}
