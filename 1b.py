#Open visual studio : File -> New -> Project -> Visualc# -> Select Window From Application Framework : .Net Framework2.0
#Right Click on References -> Add References -> Browse -> Click on Browse Button Go
#to C -> Windows -> Microsoft.Net folder >>>Select the following files :-
#Direct 3D.dll(3rd File)
#Direct 3D.dll(4th File)
#Direct X.dll(Last File)
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.DirectX;
using Microsoft.DirectX.Direct3D;

namespace p9
{
    public partial class Form1 : Form
    {
        Microsoft.DirectX.Direct3D.Device device; //OUR CODE
        Microsoft.DirectX.Direct3D.Texture texture; //OUR CODE
        Microsoft.DirectX.Direct3D.Font font; //OUR CODE

        public Form1()
        {
            InitializeComponent();
            InitDevice(); //OUR CODE
            InitFont(); //OUR CODE
            LoadTexture(); //OUR CODE
        }

        private void InitFont() //OUR CODE
        {
            System.Drawing.Font f = new System.Drawing.Font("Arial", 16f, FontStyle.Regular);
            font = new Microsoft.DirectX.Direct3D.Font(device, f);
        }

        private void LoadTexture() //OUR CODE
        {
            texture = TextureLoader.FromFile(device, "D:\\beach.jpg", 400, 400, 1, 0,
                Format.A8B8G8R8, Pool.Managed, Filter.Point, Filter.Point, Color.Transparent.ToArgb());
        }

        private void InitDevice() //OUR CODE
        {
            PresentParameters pp = new PresentParameters();
            pp.Windowed = true;
            pp.SwapEffect = SwapEffect.Discard;
            device = new Device(0, DeviceType.Hardware, this,
                CreateFlags.SoftwareVertexProcessing, pp);
        }

        private void Render() //OUR CODE
        {
            device.Clear(ClearFlags.Target, Color.Cyan, 0, 1);
            device.BeginScene();
            
            using (Sprite s = new Sprite(device))
            {
                s.Begin(SpriteFlags.AlphaBlend);
                s.Draw2D(texture, new Rectangle(0, 0, device.Viewport.Width, device.Viewport.Height), 
                    new SizeF(), new Point(0, 0), 0f, new Point(0, 0), Color.White);
                font.DrawText(s, "GAME PROGRAMMING", new Point(0, 0), Color.Black);
                s.End();
            }

            device.EndScene();
            device.Present();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render(); //OUR CODE
        }
    }
}
