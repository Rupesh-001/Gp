#Open visual studio : File -> New -> Project -> Visualc# -> Select Window From Application Framework : .Net Framework2.0
#Right Click on References -> Add References -> Browse -> Click on Browse Button Go
#to C -> Windows -> Microsoft.Net folder >>>Select the following files :-
#Direct 3D.dll(3rd File)
#Direct 3D.dll(4th File)
#Direct X.dll(Last File)
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Microsoft.DirectX;
using Microsoft.DirectX.Direct3D;

namespace GP_P1
{
    public partial class Form1 : Form
    {
        Microsoft.DirectX.Direct3D.Device device;

        public Form1()
        {
            InitializeComponent();
            InitDevice();
        }

        public void InitDevice()
        {
            PresentParameters pp = new PresentParameters();
            pp.Windowed = true;
            pp.SwapEffect = SwapEffect.Discard;
            device = new Device(0, DeviceType.Hardware, this, CreateFlags.HardwareVertexProcessing, pp);
        }

        private void Render()
        {
            device.Clear(ClearFlags.Target, Color.Orange, 0, 1);
            device.Present();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render();
        }
    }
}
