using System;
using System.Collections.Generic;
using Terraria;
using Terraria.ModLoader;
using Terraria.GameInput;
using Microsoft.Xna.Framework.Graphics;
using Terraria.DataStructures;
using Microsoft.Xna.Framework;
using Terraria.ModLoader.IO;
using Terraria.ID;
using Microsoft.Xna.Framework.Audio;
using Terraria.Utilities;
using SONICMOD.Buffs.TransformationBuffs;
using System.Linq;

namespace SONICMOD
{
    public class HPlayer : ModPlayer
    {

        #region Vars

        //class variables
        public int ChaosCrit;
        public float ChaosDamage;
        public float ChaosFlightSpeed;
        public float ChaosRunSpeed;
        public float RingCurrent;
        public float RingMax;
        public float RingMaxMult; 
        public float RingRegen;
        public float SpeedMulti;
        public float SpinDashSpeed;
        public float SpinJumpHeight;
        public int HomingAttackCount = 1;
        public float ChaosControlDuration;
        public float ChaosUsageMult;
        public float SpinDamage;
        public bool spinJumping;
        public bool homingAttack;
        public bool spinJump;
        public bool homingDash;
        public NPC closestTarget;
        public Random rand = new Random();
        public bool SuperSonic;
        public bool DarkSuperSonic;
        public bool DarkSpineSonic;
        public bool HyperSonic;
        public bool Transformed;
        public float posX;
        public float posY;
        public bool dashing;
        public uint tickCount;


        //hotkeys
        public static ModHotKey Transform;
        public static ModHotKey PowerDown;



        //skills
        public bool BallShieldUn;
        public bool ChaosBlastUn;
        public bool ChaosControUn;
        public bool ChaosExplosionUn;
        public bool ChaosSphereUn;
        public bool DarkSpineUn;
        public bool DarkSuperSonicUn;
        public bool DashUn;
        public bool FlightUn;
        public bool HomingAttackUn;
        public bool HyperSonicUn;
        public bool LightSpeedAttackUn;
        public bool TeleportUn;
        public bool SpinDashUn;
        public bool SpinJumpUn;
        public bool SuperSonicUn;

        //Acessories
        public bool AdvancedHedgehogGear;
        public bool BasicHedgehogGear;
        public bool BasicSneakers;
        public bool BigRingPounch; 
        public bool BlackQuills;
        public bool BoxingGloveLeft;
        public bool ConsumptionRing;
        public bool FusionHedgehogGear;
        public bool Gloves;
        public bool HealthRing;
        public bool LargeRingPouch;     
        public bool MagnetGloves;
        public bool MediumRingPouch;
        public bool RingBagTier1;
        public bool RingBagTier2;
        public bool RingBagTier3;
        public bool RingBagTier4;
        public bool RingCollector;
        public bool RingMultiplier;
        public bool RoughBoots;
        public bool ShovelClaws;
        public bool Skaters;
        public bool SoapShoes;
        public bool SpeedShoes;
        public bool SuperShoes;
        public bool SuperRing;
        public bool SuperRingGloves;
        public bool WallJumpShoes;
        public bool WallRunShoes;

        //items
        public bool Ring;
        public bool RingPortal;
        public bool SolidEnergy;
        public bool WispPower;
        public bool EggTech;
        public bool RingPower;
        public bool HedgehogQuill;
        public bool DarkHedgehogQuill;
        public bool AdvancedLifeformMetal;
        public bool ChaosEnergy;
        public bool SuperChaosEnergy;
        public bool DarkChaosEnergy;
        public bool EmpoweredRing;
        public bool RedSecretRing;
        public bool BlueSecretRing;
        public bool GreenSecretRing;
        public bool YellowSecretRing;
        public bool OrangeSecretRing;
        public bool PurpleSecretRing;
        public bool SilverSecretRing;
        public bool RedChaosEmerald;
        public bool BlueChaosEmerald;
        public bool GreenChaosEmerald;
        public bool YellowChaosEmerald;
        public bool OrangeChaosEmerald;
        public bool PurpleChaosEmerald;
        public bool SilverChaosEmerald;
        public bool RedSuperEmerald;
        public bool BlueSuperEmerald;
        public bool GreenSuperEmerald;
        public bool YellowSuperEmerald;
        public bool OrangeSuperEmerald;
        public bool PurpleSuperEmerald;
        public bool SilverSuperEmerald;
        public bool RedDarkEmerald;
        public bool BlueDarkEmerald;
        public bool GreenDarkEmerald;
        public bool YellowDarkEmerald;
        public bool OrangeDarkEmerald;
        public bool PurpleDarkEmerald;
        public bool SilverDarkEmerald;
        public bool MasterEmerald;
        public bool EmeraldAlter;
        public bool SuperEmeraldAlter;
        public bool RingGenerator;

        #endregion

        #region  Controls
        public bool mouseRightHeld = false;
        public bool mouseLeftHeld = false;
        public bool leftHeld = false;
        public bool rightHeld = false;
        public bool upHeld = false;
        public bool downHeld = false;
        public bool jumpHeld = false;
        public bool downTapped = false;
        public bool resetDown = false;
        #endregion
       
        
        public override void OnEnterWorld(Player player)
        {
            base.OnEnterWorld(player);
        }

        public int OverallMaxRings()
        {
            return (int)(Math.Ceiling(RingMax * RingMaxMult));
        }

        ////
        public static HPlayer ModPlayer(Player player)
        {
            return player.GetModPlayer<HPlayer>();
        }

        public override void PostUpdate()
        {
            UpdateSynchronizedControls(PlayerInput.Triggers.Current);
            ProcessSkills(player);
            if(player.velocity.Y == 0)
            {
                HitGround(player);
            }
            HandleTransformations(player);

        }

        public int getChaosDamage(int damage)
        {
            HPlayer modPlayer = player.GetModPlayer<HPlayer>();
            int originalDamage = damage;
            damage = (int)(damage * (modPlayer.ChaosDamage * player.allDamageMult));// + (player.allDamageMult - 1)));
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
            return damage;
        }

        public static void ProcessSkills(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            modPlayer.closestTarget = null;
            float closestTargetDistance = float.MaxValue;
            float distance = 0;


            #region homing
            foreach (NPC target in Main.npc)
            {
                //Get the shoot trajectory from the projectile and target
                // pass over if they're not in radius, friendly or inactive.
                distance = Vector2.Distance(player.Center, target.Center);
                if (distance > 400 || target.friendly || !target.active)
                    continue;

                if (!Collision.CanHitLine(player.Center, 0, 0, target.Center, 0, 0))
                {
                    continue;
                }

                if (distance < closestTargetDistance)//           \
                {   //---------------------------------------------\
                    closestTargetDistance = distance;//\\\\\\\\\\\\\\   
                    modPlayer.closestTarget = target;////////////////     
                }   //---------------------------------------------/
                //                                                /
                modPlayer.closestTarget.onFire2 = true;
            }
        
            
                #endregion

            if (player.justJumped)
            {
                modPlayer.spinJumping = true;
            }
            else if (modPlayer.spinJumping && modPlayer.upHeld && modPlayer.closestTarget != null && modPlayer.HomingAttackCount == 1)
            {
                modPlayer.spinJumping = false;
                modPlayer.homingAttack = true;
                modPlayer.HomingAttackCount -= 1;
            }
            else if (modPlayer.spinJumping && modPlayer.closestTarget == null && modPlayer.upHeld && modPlayer.HomingAttackCount == 1)
            {
                modPlayer.spinJumping = false;
                modPlayer.homingDash = true;
                modPlayer.HomingAttackCount -= 1;
            }

            if (modPlayer.spinJumping)
            {
                BaseSkill.SpinJump(player);
                
            }

            BaseSkill.Dash(player);
            if (modPlayer.homingAttack)
            {
                BaseSkill.HomingAttack(player, distance, modPlayer.closestTarget);
            }

            if (modPlayer.homingDash)
            {
                BaseSkill.HomingDash(player);
            }
        }

        public void HandleTransformations(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);

            if(modPlayer.DarkSuperSonic && Transform.JustPressed)
            {
                modPlayer.resetTrans(player);
                modPlayer.HyperSonic = true;
                modPlayer.Transformed = true;
            }
            if (modPlayer.DarkSpineSonic && Transform.JustPressed)
            {
                modPlayer.resetTrans(player);
                modPlayer.DarkSuperSonic = true;
                modPlayer.Transformed = true;
            }
            if (modPlayer.SuperSonic && Transform.JustPressed)
            {
                modPlayer.resetTrans(player);
                modPlayer.DarkSpineSonic = true;
                modPlayer.Transformed = true;
            }
            if (!modPlayer.Transformed && Transform.JustPressed)
            {
                modPlayer.resetTrans(player);
                modPlayer.SuperSonic = true;
                modPlayer.Transformed = true;
            }
            if(modPlayer.Transformed && PowerDown.JustPressed)
            {
                modPlayer.resetTrans(player);
            }

            //--------------------------------
            if (modPlayer.SuperSonic)
            {
                modPlayer.TurnSuper(player);
            }
            if (modPlayer.DarkSpineSonic)
            {
                modPlayer.TurnDarkSpine(player);
            }
            if (modPlayer.DarkSuperSonic)
            {
                modPlayer.TurnDarkSuper(player);
            }
            if (modPlayer.HyperSonic)
            {
                modPlayer.TurnHyper(player);
            }
            //--------------------------------
        }

        public void resetTrans(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            modPlayer.Transformed = false;
            modPlayer.SuperSonic = false;
            modPlayer.DarkSpineSonic = false;
            modPlayer.DarkSuperSonic = false;
            modPlayer.HyperSonic = false;
        }

        public HPlayer() : base()
        {

        } 
        public void UpdateSynchronizedControls(TriggersSet triggerSet)
        {
            if (triggerSet.Jump)
                jumpHeld = true;
            
            else
                jumpHeld= false;
       
            if (triggerSet.Left)
                leftHeld = true;
            else
                leftHeld = false;

            if (triggerSet.Right)
                rightHeld = true;
            else
                rightHeld = false;

            if (triggerSet.Up)
                upHeld = true;
            else
                upHeld = false;

            if (triggerSet.Down)
                downHeld = true;
            else
                downHeld = false;

            if (triggerSet.MouseRight)
                mouseRightHeld = true;
            else
                mouseRightHeld = false;

            if (triggerSet.MouseLeft)
                mouseLeftHeld = true;
            else
                mouseLeftHeld = false;

            if (triggerSet.Down && !resetDown)
            {
                downTapped = true;
                resetDown = true;
            }
            else if (resetDown)
            {
                downTapped = false;
            }
            if (player.releaseDown)
            {
                resetDown = false;
            }       
        }

        public override void ResetEffects()
        {

            //class variables
            ChaosCrit = 5;
            ChaosDamage = 1f;
            ChaosFlightSpeed = 1f;
            ChaosRunSpeed = 1f;
            RingCurrent = 0;
            RingMax = 50;
            RingMaxMult = 1f;
            RingRegen = 0f;
            SpeedMulti = 1f;
            SpinDashSpeed = 1f;
            SpinJumpHeight = 1f;
            ChaosControlDuration = 5;
            ChaosUsageMult = 1f;
            SpinDamage = 1.5f;
            spinJump = false;
            homingDash = false;
            posX = 1f;
            posY = 1f;
            dashing = false;
           // tickCount = 0;



        //Acessories
        AdvancedHedgehogGear = false;
            BasicHedgehogGear = false;
            BasicSneakers = false;
            BigRingPounch = false;
            BlackQuills = false;
            BoxingGloveLeft = false;
            ConsumptionRing = false;
            FusionHedgehogGear = false;
            Gloves = false;
            HealthRing = false;
            LargeRingPouch = false;
            MagnetGloves = false;
            MediumRingPouch = false;
            RingBagTier1 = false;
            RingBagTier2 = false;
            RingBagTier3 = false;
            RingBagTier4 = false;
            RingCollector = false;
            RingMultiplier = false;
            RoughBoots = false;
            ShovelClaws = false;
            Skaters = false;
            SoapShoes = false;
            SpeedShoes = false;
            SuperShoes = false;
            SuperRing = false;
            SuperRingGloves = false;
            WallJumpShoes = false;
            WallRunShoes = false;

            //items
            Ring = false;
            RingPortal = false;
            SolidEnergy = false;
            WispPower = false;
            EggTech = false;
            RingPower = false;
            HedgehogQuill = false;
            DarkHedgehogQuill = false;
            AdvancedLifeformMetal = false;
            ChaosEnergy = false;
            SuperChaosEnergy = false;
            DarkChaosEnergy = false;
            EmpoweredRing = false;
            RedSecretRing = false;
            BlueSecretRing = false;
            GreenSecretRing = false;
            YellowSecretRing = false;
            OrangeSecretRing = false;
            PurpleSecretRing = false;
            SilverSecretRing = false;
            RedChaosEmerald = false;
            BlueChaosEmerald = false;
            GreenChaosEmerald = false;
            YellowChaosEmerald = false;
            OrangeChaosEmerald = false;
            PurpleChaosEmerald = false;
            SilverChaosEmerald = false;
            RedSuperEmerald = false;
            BlueSuperEmerald = false;
            GreenSuperEmerald = false;
            YellowSuperEmerald = false;
            OrangeSuperEmerald = false;
            PurpleSuperEmerald = false;
            SilverSuperEmerald = false;
            RedDarkEmerald = false;
            BlueDarkEmerald = false;
            GreenDarkEmerald = false;
            YellowDarkEmerald = false;
            OrangeDarkEmerald = false;
            PurpleDarkEmerald = false;
            SilverDarkEmerald = false;
            MasterEmerald = false;
            EmeraldAlter = false;
            SuperEmeraldAlter = false;
            RingGenerator = false;

        }

        public override bool PreKill(double damage, int hitDirection, bool pvp, ref bool playSound, ref bool genGore, ref PlayerDeathReason damageSource)
        {
            if (homingAttack)
            {
                homingAttack = false;
            }
            if (spinJumping)
            {
                spinJumping = false;
            }
            return true;
        }

        public override bool PreHurt(bool pvp, bool quiet, ref int damage, ref int hitDirection, ref bool crit, ref bool customDamage, ref bool playSound, ref bool genGore, ref PlayerDeathReason damageSource)
        {

            if (homingAttack)
            {
                player.ApplyDamageToNPC(closestTarget, getChaosDamage(50), 5f, player.direction, false);
                player.velocity.X = player.direction * -5;
                player.velocity.Y = -7.5f;
                player.fullRotation = 0;
                homingAttack = false;
                return false;
            }

            return true;
        }
        public override void Hurt(bool pvp, bool quiet, double damage, int hitDirection, bool crit)
        {
            /*if (homingAttack)
            {
                player.velocity.X = 0;
                player.velocity.Y = 20;
                player.fullRotation = 0;
                homingAttack = false;
            }*/
        }

        public void HitGround(Player player)
        {
            HPlayer modPlayer = HPlayer.ModPlayer(player);
            modPlayer.homingAttack = false;
            modPlayer.spinJumping = false;
            player.fullRotation = 0;
            modPlayer.HomingAttackCount = 1;
            
        }

        public void TurnSuper(Player player)
        {
            player.AddBuff(ModContent.BuffType<Buffs.TransformationBuffs.Super>(), 5);   
        }

        public void TurnDarkSuper(Player player)
        {
                player.AddBuff(ModContent.BuffType<Buffs.TransformationBuffs.DarkSuper>(), 5);
        }

        public void TurnDarkSpine(Player player)
        {
                player.AddBuff(ModContent.BuffType<Buffs.TransformationBuffs.DarkSpine>(), 5);
        }

        public void TurnHyper(Player player)
        {
                player.AddBuff(ModContent.BuffType<Buffs.TransformationBuffs.Hyper>(), 5);
        }

        public override void PreUpdate()
        {
            
        }
    }
}
